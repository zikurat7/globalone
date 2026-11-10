from delete_usersql import main


def test_main_shows_users_before_prompt_and_deletes_selected_user(monkeypatch, capsys):
    users = [(7, "Test User", 28, "test@example.com")]
    events = []

    monkeypatch.setattr("delete_usersql.get_all_users", lambda: users)

    def prompt_for_user_id(prompt):
        events.append(("input", prompt))
        print(prompt, end="")
        return "7"

    monkeypatch.setattr("builtins.input", prompt_for_user_id)
    monkeypatch.setattr(
        "delete_usersql.delete_user",
        lambda user_id: events.append(("delete", user_id)) or True,
    )

    main()

    output = capsys.readouterr().out
    assert output.index("ID: 7") < output.index("Enter the ID")
    assert events == [
        ("input", "Enter the ID of the user to delete: "),
        ("delete", 7),
    ]
    assert "successfully deleted" in output


def test_main_does_not_prompt_when_there_are_no_users(monkeypatch, capsys):
    monkeypatch.setattr("delete_usersql.get_all_users", lambda: [])
    monkeypatch.setattr(
        "builtins.input",
        lambda _: (_ for _ in ()).throw(AssertionError("unexpected prompt")),
    )

    main()

    assert "There are no users to delete." in capsys.readouterr().out
