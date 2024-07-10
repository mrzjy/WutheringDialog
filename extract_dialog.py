import argparse
import json
import os.path

from util import load_json


def get_speaker_text(speaker_id, text_map: dict):
    speaker = text_map.get(f"Speaker_{speaker_id}_Name")
    if speaker is None:
        print(f"warning: speaker {speaker_id} not found")
    return speaker


def load_data(args):
    # text map
    text_map = load_json(os.path.join(args.repo, f"TextMap/{args.lang}/MultiText.json"))

    flow_states = load_json(os.path.join(args.repo, "ConfigDB/FlowState.json"))
    dialogs = []
    for flow in flow_states:
        flow_dict = {"title": flow["StateKey"], "actions": []}
        actions = json.loads(flow["Actions"])
        for action in actions:
            if "Params" not in action or "TalkItems" not in action["Params"]:
                action_dialog = {"id": action["ActionId"], "name": action["Name"], "type": "gameplay"}
                flow_dict["actions"].append(action_dialog)
                continue
            action_dialog = {"id": action["ActionId"], "dialogs": [], "type": "dialog"}
            for talk in action["Params"]["TalkItems"]:
                if "TidTalk" in talk:
                    # decide speaker
                    if "WhoId" in talk:
                        speaker = get_speaker_text(talk["WhoId"], text_map)
                        type_ = "dialog"
                    else:
                        speaker = ""
                        type_ = "plot"
                    action_dialog["dialogs"].append({"role": speaker, "content": text_map.get(talk["TidTalk"]), "type": type_})
                elif "Options" in talk:
                    options = []
                    for option in talk["Options"]:
                        option_dict = {"content": text_map.get(option["TidTalkOption"])}
                        if option_actions := option.get("Actions"):
                            option_dict["next_action"] = option_actions[0]["ActionId"]
                        options.append(option_dict)
                    action_dialog["dialogs"].append({"role": "player", "content": options, "type": "option"})
                else:
                    print(f"warning: Unknown talk type: {talk}")
            if action_dialog["dialogs"]:
                flow_dict["actions"].append(action_dialog)
        if flow_dict["actions"]:
            dialogs.append(flow_dict)

    with open(f"data/dialogs_{args.lang}.jsonl", "w", encoding="utf-8") as f:
        for d in dialogs:
            print(json.dumps(d, ensure_ascii=False), file=f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='D:\code\github\WutheringData')
    parser.add_argument('--lang', default='zh-Hans')
    args = parser.parse_args()

    load_data(args)