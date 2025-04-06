import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "rb") as players_data_json:
        players_data = json.load(players_data_json)

        for player_name, player_data in players_data.items():

            player_race = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"],
            )

            for skill_data in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    race=player_race[0],
                    **skill_data
                )

            player_guild = [None]

            if player_data["guild"]:
                player_guild = Guild.objects.get_or_create(
                    **player_data["guild"]
                )

            Player.objects.get_or_create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=player_race[0],
                guild=player_guild[0]
            )


if __name__ == "__main__":
    main()
