from opendbc.car.structs import CarParams
from opendbc.car.tesla.values import CAR

Ecu = CarParams.Ecu

FW_VERSIONS = {
  CAR.TESLA_MODEL_3: {
    (Ecu.eps, 0x730, None): [
      b'TeM3_E014p10_0.0.0 (16),E014.17.00',
      b'TeM3_E014p10_0.0.0 (16),EL014.17.00',
      b'TeM3_ES014p11_0.0.0 (25),ES014.19.0',
      b'TeMYG4_DCS_Update_0.0.0 (13),E4014.28.1',
      b'TeMYG4_DCS_Update_0.0.0 (9),E4014.26.0',
      b'TeMYG4_Legacy3Y_0.0.0 (2),E4015.02.0',
      b'TeMYG4_Legacy3Y_0.0.0 (5),E4015.03.2',
      b'TeMYG4_Main_0.0.0 (59),E4H014.29.0',
      b'TeMYG4_Main_0.0.0 (65),E4H015.01.0',
      b'TeMYG4_Main_0.0.0 (67),E4H015.02.1',
      b'TeMYG4_SingleECU_0.0.0 (33),E4S014.27',
    ],
  },
  CAR.TESLA_MODEL_Y: {
    (Ecu.eps, 0x730, None): [
      b'TeM3_E014p10_0.0.0 (16),Y002.18.00',
      b'TeM3_E014p10_0.0.0 (16),YP002.18.00',
      b'TeM3_ES014p11_0.0.0 (16),YS002.17',
      b'TeM3_ES014p11_0.0.0 (25),YS002.19.0',
      b'TeMYG4_DCS_Update_0.0.0 (13),Y4002.27.1',
      b'TeMYG4_DCS_Update_0.0.0 (13),Y4P002.27.1',
      b'TeMYG4_DCS_Update_0.0.0 (9),Y4P002.25.0',
      b'TeMYG4_Legacy3Y_0.0.0 (2),Y4003.02.0',
      b'TeMYG4_Legacy3Y_0.0.0 (5),Y4003.03.2',
      b'TeMYG4_Legacy3Y_0.0.0 (2),Y4P003.02.0',
      b'TeMYG4_SingleECU_0.0.0 (33),Y4S002.26',
    ],
  },
  CAR.TESLA_MODEL_S_PREAP: {
    # Pre-Autopilot Model S fingerprints from CAN bus
    # These vehicles lack the sophisticated ECU fingerprinting of newer Tesla models
    # Identification primarily relies on CAN message patterns
  },
}

FINGERPRINTS = {
  CAR.TESLA_MODEL_S_PREAP: [{
    # Pre-AP Model S fingerprint from tinkla - 2013 base model
    1: 8, 3: 8, 14: 8, 21: 4, 69: 8, 109: 4, 257: 3, 264: 8, 277: 6, 280: 6, 293: 4, 296: 4, 309: 5, 325: 8, 336: 8, 341: 8, 360: 7, 373: 8, 389: 8, 415: 8, 513: 5, 516: 8, 520: 4, 522: 8, 524: 8, 527: 8, 536: 8, 551: 4, 552: 2, 556: 8, 568: 8, 582: 5, 638: 8, 643: 8, 693: 8, 696: 8, 712: 8, 728: 8, 744: 8, 760: 8, 771: 2, 772: 8, 775: 8, 776: 8, 778: 8, 780: 2, 783: 8, 785: 8, 787: 8, 788: 8, 791: 8, 792: 8, 796: 2, 799: 8, 804: 8, 805: 8, 807: 8, 808: 1, 812: 8, 815: 8, 820: 8, 823: 8, 824: 8, 831: 8, 836: 8, 840: 8, 856: 4, 863: 8, 872: 8, 880: 8, 888: 8, 896: 8, 901: 6, 904: 3, 920: 8, 936: 8, 949: 8, 952: 8, 953: 6, 968: 8, 984: 8, 1000: 8, 1006: 8, 1026: 8, 1028: 8, 1029: 8, 1030: 8, 1032: 1, 1034: 8, 1048: 1, 1064: 8, 1080: 8, 1281: 8, 1285: 8, 1332: 8, 1335: 8, 1362: 6, 1368: 8, 1412: 8, 1436: 8, 1456: 8, 1463: 8, 1476: 8, 1524: 8, 1527: 8, 1601: 8, 1605: 8, 1617: 8, 1621: 8, 1800: 4, 1804: 8, 1812: 8, 1815: 8, 1816: 8, 1828: 8, 1831: 8, 1832: 8, 1840: 8, 1848: 8, 1864: 8, 1880: 8, 1892: 8, 1896: 8, 1912: 8, 1960: 8, 1992: 8, 2008: 3, 2043: 5
  }],
}