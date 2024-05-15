from user_agents import parse


def get_user_agenet_details(user_agent_string: str):
    user_agent = parse(user_agent_string)

    return {
        'browser': {
            'name': user_agent.browser.family,
            'version': user_agent.browser.version_string,
        },
        'operating_system': {
            'name': user_agent.os.family,
            'version': user_agent.os.version_string,
        },
        'device': {
            'type': user_agent.device.family,
            'is_mobile': user_agent.is_mobile,
            'is_tablet': user_agent.is_tablet,
            'is_pc': user_agent.is_pc,
        }
    }

# ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# print(get_user_agenet_details(ua_string))