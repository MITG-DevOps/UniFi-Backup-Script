from unifi_backup_settings import UISettings
# from selenium_scripts import backup_network_settings_current_UI_selenium, backup_OS_settings_current_UI_selenium

def get_device_information():
    unifi_device_information: dict[str, dict[str, ]] = {

#'Ascent / White Birch':		{'ip': '68D79A2579C800000000052DF3C200000000056A235B000000005FB4314D:338187428',},
'Ascent Fine Cabinetry':	{'ip': '28704E376EBF000000000827D4FA0000000008968700000000006685A4F2:540183858',},
'BeNice':			{'ip': '784558C0074500000000061E3EB20000000006663270000000006169688F:1537113996',},
'Blossom Hotel':		{'ip': '9C05D6C0E0D7000000000810067400000000087D89F7000000006645D3E0:1400431108',},
'Bonnell': 			{'ip': '9C05D66145F50000000007F758070000000008633CF20000000065F28E2C:88797900',},
'Borisch_GR': 			{'ip': 'E43883819CB100000000074E00340000000007A7027C0000000063F1D9E9:310078493',},
#'CRH': 				{'ip': '39c6b9f3-8a98-4fa6-a658-f806fcabd0af:685193060',},
'DiLeonardoHome': 		{'ip': 'D021F9DD975100000000066ADC7D0000000006B7A795000000006280CD80:1731261386',},
'DLS-GH': 			{'ip': '7845588730BD000000000604073400000000064AB0CE000000006134ED42:541963461',},
'DLS-GR': 			{'ip': '7483C2D065BD00000000042FD72300000000045D4A4E000000005D5FF35F:293309390',},
'Envision': 			{'ip': '68D79A60891500000000058596B50000000005C60957000000006050F3A5:1626597121',},
'EXE-Mac02': 			{'ip': '70A741E4C167000000000692A6280000000006E1B7A40000000062E19625:1887360423',},
'GHP Grand Rapids': 		{'ip': 'D021F9DDFF2500000000066B35710000000006B80D66000000006282551C:784918383',},
'GHP Petoskey': 		{'ip': 'D021F9DDFF2500000000066B35710000000006B80D66000000006282551C:784918383',},
'GRB': 				{'ip': '602232E809BB0000000006D96CC400000000072C17B30000000063582DF7:931486536',},
'GRCM-DMP': 			{'ip': 'E4388340D08300000000072FE011000000000786F2850000000063BD0E73:1156565869',},
'GRCT - Default': 		{'ip': 'D021F9705E5B000000000649CE62000000000694A16E00000000620AB9E7:2101998349',},
'GRCT - GR': 			{'ip': 'D021F9705E5B000000000649CE62000000000694A16E00000000620AB9E7:2101998349',},
'GRS': 				{'ip': 'D021F951E97300000000063CE7AD000000000686E2A10000000061C7ED86:1490215287',},
'HF-GH': 			{'ip': '7483C2D626EB00000000043F418700000000046DCA63000000005D8F36DC:345506707',},
'HF-HOL': 			{'ip': '7483C2D6281900000000043F200E00000000046DA699000000005D8ED909:1192199007',},
'HLL': 				{'ip': 'D021F97040270000000006481738000000000692CEA00000000062040312:604923036',},
'Icon-Gen2': 			{'ip': '74ACB946C3090000000004BADBC50000000004F097D9000000005ECD590D:532058248',},
'Inhulsen Law': 		{'ip': '70A741F973010000000006B7B647000000000708BF130000000063262D53:752854159',},
'JP-Office': 			{'ip': '784558ECD71F0000000006320BEC00000000067B19B80000000061A148AE:1955348600',},
'JPA': 				{'ip': '74ACB93DA90B0000000004B051A70000000004E5B2BE000000005EBCC470:1254341210',},
'KDDS': 			{'ip': 'D021F9648087000000000644372C00000000068EB6210000000061E9A0AC:301312777',},
'LFG': 				{'ip': '602232FA2A790000000006DCEF7800000000072FBB7800000000635B7E3A:623111119',},
'LHM Partners': 		{'ip': 'F4E2C6EB89270000000007DA2BC6000000000842244A00000000656C3210:485376217',},
'Maple Tower': 			{'ip': 'AC8BA952A3110000000007025A23000000000756A9D70000000063801FD0:288332091',},
'McKayTower': 			{'ip': '245A4C8A2AC30000000005DF7F5E0000000006240F8A0000000060E90996:1324882433',},
'MCVB': 			{'ip': '9C05D6D55F9500000000081A0B20000000000888150C000000006662CB28:360056432',},
'MFD': 				{'ip': '602232AF655B0000000006CC17EE00000000071E267700000000634997AF:46652881',},
'MITG-CK2': 			{'ip': 'F4E2C6E6CA890000000007D3C39700000000083AF201000000006558DA0A:2033680971',},
'MOD-GR': 			{'ip': '7483C2778A4B00000000041DE8CB00000000044A8C96000000005D2C073D:175724524',},
'MOD-SRO': 			{'ip': '70A741E6653D000000000693692A0000000006E28AFB0000000062E2D012:270076739',},
'MOD-WMEM': 			{'ip': '70A741E95DF900000000069A7F8B0000000006EA0FCB0000000062F232FA:1723148007',},
'NShore': 			{'ip': '68D79A505E5D000000000572FEF40000000005B29CB70000000060362EFF:1522883505',},
'OGS': 				{'ip': 'D021F951EB0D00000000063CFC45000000000686F8AE0000000061C83959:709222073',},
'Purforms-UDM': 		{'ip': 'b53deea5-b011-45a0-9acf-927e9a35b6e5',},
'PF UNVR': 			{'ip': 'AC8BA95155CD000000000701CD47000000000756158900000000637F8F79:1977057233',},
'Tuinstra': 			{'ip': 'D021F9C9B32700000000065F794A0000000006ABAC0100000000625D6DF3:902470032',},
'Tuinstra-BlueLake': 		{'ip': '9C05D64CAEF30000000007EF05FD000000000859CD0B0000000065CD8DE8:696183732',},
'PPCorp': 			{'ip': '70A741E6645D000000000693476D0000000006E2663C0000000062E29AA4:707751101',},
'PeppinosPizzaDowntown': 	{'ip': '18E8294F85EF0000000003D3455B0000000003FB9980000000005C4DAE94:1227678311',},
'Peppinos-Standale': 		{'ip': '7483C2D6251700000000043F4C1A00000000046DD571000000005D8F5BCF:229011829',},
'PP-South': 			{'ip': '049f1989-4f36-43f7-8cf9-24395a4c14a6:541770914',},
'RANT-Allendale': 		{'ip': '245A4C7D33F50000000005D0116E000000000613DD090000000060C46B8D:490964096',},
'RANT-GR-Cascade': 		{'ip': '7483C27B5761000000000427FEA700000000045515B4000000005D4A3EE9:286643898',},
'SAM-GRR': 			{'ip': 'F09FC21C3A9F000000000260974F000000000277409600000000589DC70A:1302455877',},
'SAM-KZ': 			{'ip': '70A741A1193F00000000067E0E150000000006CBE2E30000000062B7260A:187143308',},
'ScarlettHome': 		{'ip': 'E438833D0CC9000000000734E0C000000000078C3CE90000000063C36C0A:1431601224',},
'ScarlettInc-DMP': 		{'ip': 'E4388319DB8B000000000716C35900000000076C3929000000006398CB8C:1975248318',},
'SCI-Advisors': 		{'ip': '245A4C8E4E890000000005E1F56E000000000626B0FE0000000060EF43FB:1522882506',},
'Sibsco-CK2': 			{'ip': '9C05D66EE3B90000000007FE87F900000000086B10DA000000006606EA1D:96344610',},
'KVFD': 			{'ip': 'F4E2C6E6B2510000000007D519EF00000000083C76C100000000655C8390:1705722467',},
'TC': 				{'ip': '70A741E6662D000000000693769E0000000006E299C80000000062E2E2CA:1544670769',},
'TournellFD': 			{'ip': 'F4E2C6DB57090000000007CD210D00000000083378E2000000006549963F:1829459095',},
'TRI': 				{'ip': 'D021F979A30900000000064CB71A000000000697C0930000000062183431:2090346760',},
'VBG': 				{'ip': '70A741EE17D90000000006A297A10000000006F287F20000000063007A0D:2016404772',},
'VibrantFutures': 		{'ip': '68D79A2B695B00000000053735C6000000000573E0D0000000005FC37912:1115520691',},
'WS-CKG2+': 			{'ip': 'FCECDA4842E70000000003153C46000000000334E9DD000000005ABFA879:1442309194',},

    }
    return unifi_device_information
