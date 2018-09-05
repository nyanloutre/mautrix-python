from mautrix_appservice import AppService


def _new_token() -> str:
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(64))


def registration() -> dict:
    return {
        "id": self["appservice.id"] or "telegram",
        "as_token": self["appservice.as_token"],
        "hs_token": self["appservice.hs_token"],
        "namespaces": {
            "users": [{
                "exclusive": True,
                "regex": f"@{username_format}:{homeserver}"
            }],
            "aliases": [{
                "exclusive": True,
                "regex": f"#{alias_format}:{homeserver}"
            }]
        },
        "url": self["appservice.address"],
        "sender_localpart": self["appservice.bot_username"],
        "rate_limited": False
    }


appserv = AppService("https://matrix.local", "matrix.local",
                     config["appservice.as_token"], config["appservice.hs_token"],
                     config["appservice.bot_username"], log="mau.as", loop=loop,
                     verify_ssl=config["homeserver.verify_ssl"], state_store=state_store,
                     real_user_content_key="net.maunium.telegram.puppet",
                     aiohttp_params={
                         "client_max_size": config["appservice.max_body_size"] * mebibyte
                     })
