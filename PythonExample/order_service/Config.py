# setting about combobox
PRIMESET = (
    "上市櫃", "興櫃",
)

BUYSELLSET = (
    "買進", "賣出",
)

PERIODSET = dict(
    stock = ("盤中", "盤後", "零股"),
    future = ("ROD", "IOC", "FOK"),
    sea_future = ("ROD"),
    moving_stop_loss = ("IOC", "FOK"),
)

STRADETYPE = dict(
    sea_future = ("LMT（限價）", "MKT（市價）", "STL（停損限價）", "STP（停損市價）"),
    sea_option = ("LMT（限價）"),
)

FLAGSET = dict(
    stock = ("現股", "融資", "融券", "無券"),
    future = ("非當沖", "當沖"),
)

NEWCLOSESET = dict(
    future = ("新倉", "平倉", "自動"),
    sea_future = ("新倉"),
    option_future = ("新倉", "平倉")
)

RESERVEDSET = (
    "盤中", "T盤預約",
)

CALLPUTSET = (
    "CALL", "PUT",    
)

ACCOUNTTYPESET = (
    "外幣專戶", "台幣專戶",
)

CURRENCYSET = (
    "HKD", "NTD", "USD", "JPY", "SGD", "EUR", "AUD",
)

EXCHANGENOSET = (
    "美股",   
)
