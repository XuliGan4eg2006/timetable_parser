x_offset = 5
y_offset = 5

filter_words = ["ауд.", "ДНИ\nНЕДЕЛИ", "ГРУППА\nпара"]

selected_page = "01.04-06.04"

#download_url = "https://docs.google.com/spreadsheets/d/16uSGpWqO6d9UR3clLbBeAj_bSaYPWxLZ/export?format=xlsx"
download_url = "https://docs.google.com/spreadsheets/d/1oet97f5tYfG4Z4MkX943S7D_3mjlLIcUTUwEcbgNcZ8/export?format=xlsx"
groups = ['ИСП9-123А', 'ИСП9-123Б', 'ИСП9-123В', 'ИСП9-123Г', 'ИСП9-123П', 'ОИБ9-123А', 'ОИБ9-123Б', 'ОИБ9-123В', 'ИСС9-123А', 'ИСС9-123Б', 'ССА9-123А', 'ССА9-123Б', 'ССА9-123В', 'СР9-123', 'ССА11-123П', 'ИСП11-123АП', 'ИСП11-123БП', 'ОИБ11-123П', 'ИСС9-222А', 'ИСС9-222Б', 'ИСС9-222В', 'Р9-222А', 'Р9-222Б', 'ОИБ9-222А', 'ОИБ9-222Б', 'ОИБ9-222В', 'ОИБ9-222П', 'ИСП9-222А', 'ИСП9-222Б', 'ИСП9-222АП', 'ИСП9-222БП', 'ИСП9-222ВП', 'ССА9-222А', 'ССА9-222Б', 'ССА9-222В', 'ССА9-222П', 'ИСП11-222АП', 'ИСП11-222БП', 'ИСП11-222ВП', 'ИСП9-321А', 'ИСП9-321Б', 'ИСП9-321АП', 'ИСП9-321БП']

breaks = ["Перемена 10 минут", "Перемена 30 минут", "Перемена 30 минут", "Перемена 10 минут", "Перемена 10 минут",
          "Конец пар"]

group_map = {
    "ИСП9-123А": "C",
    "ИСП9-123Б": "F",
    "ИСП9-123В": "I",
    "ИСП9-123Г": "L",
    "ИСП9-123П": "O",
    "ОИБ9-123А": "T",
    "ОИБ9-123Б": "W",
    "ОИБ9-123В": "Z",
    "ИСС9-123А": "AC",
    "ИСС9-123Б": "AF",
    "ССА9-123А": "AK",
    "ССА9-123Б": "AN",
    "ССА9-123В": "AQ",
    "СР9-123": "AT",
    "ССА11-123П": "AW",
    "ИСП11-123АП": "BA",
    "ИСП11-123БП": "BD",
    "ОИБ11-123П": "BG",
    "ИСС9-222А": "BL",
    "ИСС9-222Б": "BO",
    "ИСС9-222В": "BR",
    "Р9-222А": "BU",
    "Р9-222Б": "BX",
    "ОИБ9-222А": "CC",
    "ОИБ9-222Б": "CF",
    "ОИБ9-222В": "CI",
    "ОИБ9-222П": "CL",
    "ИСП9-222А": "CQ",
    "ИСП9-222Б": "CT",
    "ИСП9-222АП": "CW",
    "ИСП9-222БП": "CZ",
    "ИСП9-222ВП": "DC",
    "ССА9-222А": "DH",
    "ССА9-222Б": "DK",
    "ССА9-222В": "DN",
    "ССА9-222П": "DQ",
    "ИСП11-222АП": "DV",
    "ИСП11-222БП": "DY",
    "ИСП11-222ВП": "EB",
    #"ССА11-222П": "EI",
    #"ОИБ11-222АП": "EL",
    #"ОИБ11-222БП": "EO",
    #"ОИБ9-321А": "ET",
    #"ОИБ9-321Б": "EW",
    #"ОИБ9-321В": "EZ",
    #"ОИБ9-321П": "FC",
    "ИСП9-321А": "FF",
    "ИСП9-321Б": "FI",
    "ИСП9-321АП": "FL",
    "ИСП9-321БП": "FO",
    # "ИСС9-321А": "FV",
    # "ИСС9-321Б": "FY",
    # "ИСС9-321В": "GB",
    # "ИСС9-321Г": "GE",
    # "Р9-321": "GH",
    # "ССА9-321А": "GM",
    # "ССА9-321Б": "GP",
    # "ССА11-321П": "GU",
    # "ИСП11-321АП": "GX",
    # "ИСП11-321БП": "HA",
    # "ИСП11-321ВП": "HD",
    # "ОИБ11-321АП": "HG",
    # "ОИБ11-321БП": "HJ",
    # "ИСП9-420АП": "HO",
    # "ИСП9-420БП": "HR",
    # "ОИБ9-420П": "HU",
    # "ИСС9-420П": "HX"
}