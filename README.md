# WutheringDialog
A simple project that extracts character conversations in Wuthering Waves game.

这是一个抽取鸣潮对话语料的小项目

Thanks to [Dimbreath's project](https://github.com/Dimbreath/WutheringData/tree/master).

We're currently able to parse some dialogs for quests, including 3 content types: character dialogs, player options, and plot narrations.

The dialogs are in chatgpt-message format, with role and content fields for each utterance.

## Steps

1. Get WutheringData from [Dimbreath's project](https://github.com/Dimbreath/WutheringData/tree/master), you could git clone or download the zip and extract it.

2. Run extract_dialog.py, resulting in output files in "data" folder

- Example command line

```
python extract_dialog.py \
    --repo=PATH/TO/WutheringData \
    --lang=zh-Hans
```

**Note:** The "--lang" argument can be one of the language options from WutheringData/TextMap's subdirectories.  

- The resulting data example

(You need to run the command yourself to get **FULL** data, the data folder in this github repo contains only examples.)

```json
{
  "title": "剧情_角色_忌炎线_4_5",
  "actions": [
    {
      "id": 5000220,
      "name": "SetPlotMode",
      "type": "gameplay"
    },
    {
      "id": 5000180,
      "name": "FadeInScreen",
      "type": "gameplay"
    },
    ...
    {
      "id": 5000185,
      "dialogs": [
        {
          "role": "player",
          "content": [
            {
              "content": "忌炎。"
            }
          ],
          "type": "option"
        },
        {
          "role": "忌炎",
          "content": "有件事，我希望你能和我一起完成。",
          "type": "dialog"
        },
        {
          "role": "忌炎",
          "content": "一颗种子。",
          "type": "dialog"
        },
        {
          "role": "忌炎",
          "content": "这是我多年前拜托研究院培育的花种，研究院曾告诉我，它的生命力十分顽强。",
          "type": "dialog"
        },
        ...
        {
          "role": "",
          "content": "你收下了这颗种子，明明很小，握在手中却十分沉重。",
          "type": "plot"
        },
        {
          "role": "",
          "content": "你们将它种下，也许某天，它也会与你们一起眺望今州城的夕阳。",
          "type": "plot"
        },
        {
          "role": "player",
          "content": [
            {
              "content": "事情都解决了吗？",
              "next_action": 5000186
            },
            {
              "content": "你还好吗？",
              "next_action": 5000193
            }
          ],
          "type": "option"
        },
        {
          "role": "忌炎",
          "content": "目前来看，这次残象潮爆发的风险，是解决了。",
          "type": "dialog"
        },
        {
          "role": "忌炎",
          "content": "但潜伏在瑝珑深处的敌人……仍在蠢蠢欲动，我们对于“它”还是缺乏足够的了解。",
          "type": "dialog"
        },
        
      ],
      "type": "dialog"
    },
    {
      "id": 5000238,
      "name": "FadeOutScreen",
      "type": "gameplay"
    }
    ...
  ]
}
```

## FAQs

1. Interested in some game corpus?

- [GenshinDialog](https://github.com/mrzjy/GenshinDialog)
- [StarrailDialog](https://github.com/mrzjy/StarrailDialogue)
- [ArknightsDialog](https://github.com/mrzjy/ArknightsDialog)
- [WutheringDialog](https://github.com/mrzjy/WutheringDialog)
- [hoyo_public_wiki_parser](https://github.com/mrzjy/hoyo_public_wiki_parser): Parse Hoyoverse public wiki data
