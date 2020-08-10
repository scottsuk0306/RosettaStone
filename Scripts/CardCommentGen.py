import json


def cardCommentGen(card):
    div = "\n// --------------------------------------------------------"
    comm = "\n// "
    str_format = "//#"+'%56s' % ("#"+card['type']+"#-#"+card['cardClass'])
    str_format = str_format.replace(" ", "-")
    str_format = str_format.replace("#", " ")
    str_format = str_format + comm + "[" + card['id'] + "] " + card['name'] + " - COST: "
    if("cost" in card.keys()):
        str_format = str_format + str(card['cost'])
    else:
        str_format = str_format + str(0)
    if card['type'] == "MINION":
        str_format = str_format + " [ATK: " + str(card['attack']) + "/HP: " + str(card['health']) + "]"
    str_format = str_format + comm + " - "
    if "race" in card.keys():
        str_format = str_format + "Race: " + card['race']+", "
    if "faction" in card.keys():
        str_format = str_format + "Faction: " + card['faction']+", "
    str_format = str_format + "Set: " + card['set']
    if "rarity" in card.keys():
        str_format = str_format+", " + "Rarity: " + card['rarity'].capitalize()
    str_format = str_format + div
    if "text" in card.keys():
        card['text'] = card['text'].replace("[x]","")
        card['text'] = card['text'].replace("$","")
        card['text'] = card['text'].replace("\n","\n//       ")
        str_format = str_format + comm + "Text: " + card['text'] + div
    # if card has GameTag, PlayReq, or RefTag, add it.
    # GameTag
    if "mechanics" in card.keys() or "elite" in card.keys():
        str_format = str_format + comm + "GameTag:"
        if "elite" in card.keys():
            str_format = str_format + comm + " - ELITE = 1"
        if "mechanics" in card.keys():
            for tag in card['mechanics']:
                str_format =  str_format + comm + " - " + tag + " = 1"
            str_format = str_format + div
    # How About PlayReq?

    # RefTag
    if "referencedTags" in card.keys():
        str_format = str_format + comm + "RefTag:"
        if "referencedTags" in card.keys():
            for tag in card['referencedTags']:
                str_format = str_format + comm + " - "  + tag + " = 1"
            str_format = str_format + div
    return str_format


def setCommentGen(target_set, target_id):
    Heroes = []
    HeroPowers = []
    Druid = []
    DruidNonCollect = []
    Hunter = []
    HunterNonCollect = []
    Mage = []
    MageNonCollect = []
    Paladin = []
    PaladinNonCollect = []
    Priest = []
    PriestNonCollect = []
    Rogue = []
    RogueNonCollect = []
    Shaman = []
    ShamanNonCollect = []
    Warlock = []
    WarlockNonCollect = []
    Warrior = []
    WarriorNonCollect = []
    DemonHunter = []
    DemonHunterNonCollect = []
    Dual = []
    DualNonCollect = []
    Neutral = []
    NeutralNonCollect = []

    all = [Heroes, HeroPowers, Druid, DruidNonCollect, Hunter, HunterNonCollect, Mage,
           MageNonCollect, Paladin, PaladinNonCollect, Priest, PriestNonCollect,
           Rogue, RogueNonCollect, Shaman, ShamanNonCollect, Warlock, WarlockNonCollect,
           Warrior, WarriorNonCollect, DemonHunter, DemonHunterNonCollect, Dual, DualNonCollect,
           Neutral, NeutralNonCollect]

    all_names = ["Heroes", "HeroPowers", "Druid", "DruidNonCollect", "Hunter", "HunterNonCollect", "Mage",
                 "MageNonCollect", "Paladin", "PaladinNonCollect", "Priest", "PriestNonCollect",
                 "Rogue", "RogueNonCollect", "Shaman", "ShamanNonCollect", "Warlock", "WarlockNonCollect",
                 "Warrior", "WarriorNonCollect", "DemonHunter", "DemonHunterNonCollect", "Dual", "DualNonCollect",
                 "Neutral", "NeutralNonCollect"]
    # coding=utf8
    file_path = "../Resources/cards.json"
    with open(file_path, "r", encoding='UTF8') as json_file:
        card_data = json.load(json_file)
    # Empty the list
    total_cnt = 0
    collectible_cnt = 0
    for card in card_data:
        if card['id'].split("_")[0] != target_set:
            continue
        # count the number of cards in target set
        total_cnt+=1
        if "collectible" in card.keys() and card["collectible"] == True:
            collectible_cnt += 1

        if card["type"] == "HERO":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            Heroes.append(data)
        elif card["type"] == "HERO_POWER":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            HeroPowers.append(data)
        elif "cardClass" not in card.keys():
            # Exception
            continue
        elif card["cardClass"] == "DRUID":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Druid.append(data)
            else:
                DruidNonCollect.append(data)

        elif card["cardClass"] == "HUNTER":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Hunter.append(data)
            else:
                HunterNonCollect.append(data)
        elif card["cardClass"] == "MAGE":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Mage.append(data)
            else:
                MageNonCollect.append(data)
        elif card["cardClass"] == "PALADIN":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Paladin.append(data)
            else:
                PaladinNonCollect.append(data)
        elif card["cardClass"] == "PRIEST":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Priest.append(data)
            else:
                PriestNonCollect.append(data)
        elif card["cardClass"] == "ROGUE":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Rogue.append(data)
            else:
                RogueNonCollect.append(data)
        elif card["cardClass"] == "SHAMAN":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Shaman.append(data)
            else:
                ShamanNonCollect.append(data)
        elif card["cardClass"] == "WARLOCK":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Warlock.append(data)
            else:
                WarlockNonCollect.append(data)
        elif card["cardClass"] == "WARRIOR":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Warrior.append(data)
            else:
                WarriorNonCollect.append(data)
        elif card["cardClass"] == "DEMONHUNTER":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                DemonHunter.append(data)
            else:
                DemonHunterNonCollect.append(data)
        elif card["cardClass"] == "DUAL":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Dual.append(data)
            else:
                DualNonCollect.append(data)
        elif card["cardClass"] == "NEUTRAL":
            data = cardCommentGen(card)
            data = data + "\n" + "\n"
            if "collectible" in card.keys() and card["collectible"]:
                Neutral.append(data)
            else:
                NeutralNonCollect.append(data)

    name = iter(all_names)
    with open(target_set+"_comment"+".txt", 'a', -1, 'utf-8') as f:
        f.write('test data line')
        for group in all:
            f.write(next(name))
            f.write(" =" * 57 + "\n\n\n")
            for data in group:
                f.write(data)
        f.close()
    return total_cnt, collectible_cnt

if __name__ == '__main__':
    # Sample Input
    # Enter the ID of Set to generate comments (ex: BT, YOD, ULD .. etc): BT
    # Total of 261 card comments are generated

    target_set = input("Enter the first ID of Set to generate comments (ex: BT, YOD, ULD .. etc): ")
    target_set = target_set.upper()
    total_count, collectible_count = setCommentGen(target_set)
    print("Total of {total_count} card comments are generated. "
          "\nTotal of {collectible_count} collectible card comments are generated.\n".
          format(total_count=total_count, collectible_count=collectible_count))
