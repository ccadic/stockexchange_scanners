import yfinance as yf
from tabulate import tabulate
from datetime import datetime, timedelta
import pandas as pd

def calculate_progression(data, period):
    start_price = data.iloc[0]['Close']
    end_price = data.iloc[-1]['Close']
    return ((end_price - start_price) / start_price) * 100

def get_stock_data(symbol, period):
    end_date = datetime.today()
    start_date = end_date - period
    return yf.download(symbol, start=start_date, end=end_date)

def main():
    companies = {
        "Aton Resources Inc.": "AAN",
        "ATI Airtest Technologies Inc.": "AAT",
        "Aben Minerals Ltd.": "ABM",
        "Arbor Metals Corp.": "ABR",
        "Aurora Solar Technologies Inc.": "ACU",
        "Arctic Star Exploration Corp.": "ADD",
        "Adamera Minerals Corp.": "ADZ",
        "American Eagle Gold Corp.": "AE",
        "Atlas Engineered Products Ltd.": "AEP",
        "Silver X Mining Corp.": "AGX",
        "Amarc Resources Ltd.": "AHR",
        "Clean Air Metals Inc.": "AIR",
        "Ackroo Inc.": "AKR",
        "ALX Resources Corp.": "AL",
        "Alpha Exploration Ltd.": "ALEX",
        "Alturas Minerals Corp": "ALT",
        "Alvopetro Energy Ltd.": "ALV",
        "Abacus Mining & Exploration Corporation": "AME",
        "American Creek Resources Ltd.": "AMK",
        "Amex Exploration Inc.": "AMX",
        "Andean Precious Metals Corp.": "APM",
        "ARCpoint Inc.": "ARC",
        "Arch Biopartners Inc.": "ARCH",
        "Aurum Lake Mining Corporation.": "ARL",
        "Aurora Spine Corporation": "ASG",
        "Astra Exploration Inc.": "ASTR",
        "Altai Resources Inc": "ATI",
        "Atomic Minerals Corporation": "ATOM",
        "Aurion Resources Ltd": "AU",
        "Advent-AWI Holdings Inc.": "AWI",
        "Arcwest Exploration Inc.": "AWX",
        "Arrow Exploration Corp.": "AXL",
        "BCM Resources Corporation": "B",
        "Beacn Wizardry & Magic Inc.": "BECN",
        "Baroyeca Gold & Silver Inc.": "BGS",
        "Hercules Silver Corp.": "BIG",
        "Big Tree Carbon Inc.": "BIGT",
        "BuildDirect.Com Technologies Inc.": "BILD",
        "Thunderbird Minerals Corp.": "BIRD",
        "Blue Thunder Mining Inc.": "BLUE",
        "Battery Mineral Resources Corp.": "BMR",
        "The Limestone Boat Company Limited": "BOAT",
        "Backstageplay Inc.": "BP",
        "Blackrock Silver Corp.": "BRC",
        "Barksdale Resources Corp.": "BRO",
        "Bravo Mining Corp.": "BRVO",
        "Brunswick Exploration Inc.": "BRW",
        "Bluestone Resources Inc.": "BSR",
        "Bessor Minerals Inc.": "BST",
        "Bitcoin Well Inc.": "BTCW",
        "Bonterra Resources Inc.": "BTR",
        "Bitterroot Resources Ltd.": "BTT",
        "BTU Metals Corp.": "BTU",
        "Benz Mining Corp.": "BZ",
        "Canaf Investments Inc.": "CAF",
        "Composite Alliance Group Inc.": "CAG",
        "Canadabis Capital Inc.": "CANB",
        "Capitan Silver Corp.": "CAPT",
        "Champion Bear Resources Ltd.": "CBA",
        "Colibri Resource Corporation": "CBI",
        "Canada Carbon Inc.": "CCB",
        "Cascadero Copper Corporation": "CCD",
        "Coelacanth Energy Inc.": "CEI",
        "Canadian Gold Corp.": "CGC",
        "Central Iron Ore Limited": "CIO",
        "Clip Money Inc.": "CLIP",
        "Consolidated Lithium Metals Inc.": "CLM",
        "Cielo Waste Solutions Corp.": "CMC",
        "C-COM Satellite Systems Inc.": "CMI",
        "Comet Industries Ltd.": "CMU",
        "Canada Nickel Company Inc.": "CNC",
        "California Nanotechnologies Corp": "CNO",
        "Contagious Gaming Inc.": "CNS",
        "Callinex Mines Inc.": "CNX",
        "Coast Copper Corp.": "COCO",
        "Ostrom Climate Solutions Inc.": "COO",
        "Camino Minerals Corporation": "COR",
        "CopperCorp Resources Inc.": "CPER",
        "Canadian Premium Sand Inc.": "CPS",
        "Churchill Resources Inc.": "CRI",
        "Centaurus Energy Inc.": "CTA",
        "Canterra Minerals Corporation": "CTM",
        "Canalaska Uranium Ltd.": "CVV",
        "Cematrix Corporation": "CVX",
        "Cytophage Technologies Ltd.": "CYTO",
        "Datable Technology Corporation": "DAC",
        "Arianne Phosphate Inc.": "DAN",
        "Darelle Online Solutions Inc.": "DAR",
        "Decibel Cannabis Company Inc.": "DB",
        "Decisive Dividend Corporation": "DE",
        "Decade Resources Ltd.": "DEC",
        "Defiance Silver Corp.": "DEF",
        "Dixie Gold Inc.": "DG",
        "Digihost Technology Inc.": "DGHI",
        "Discovery Harbour Resources Corp.": "DHR",
        "Margaret Lake Diamonds Inc.": "DIA",
        "Decklar Resources Inc.": "DKL",
        "Delta Resources Limited": "DLTA",
        "Datametrex AI Limited": "DM",
        "CloudMD Software & Services Inc.": "DOC",
        "Destiny Media Technologies Inc.": "DSY",
        "Dolly Varden Silver Corporation": "DV",
        "CardioComm Solutions, Inc.": "EKG",
        "Electra Battery Materials Corporation": "ELBM",
        "Elysee Development Corp.": "ELC",
        "Electric Metals (USA) Limited": "EML",
        "Giyani Metals Corp.": "EMM",
        "Euro Manganese Inc.": "EMN",
        "Eminent Gold Corp.": "EMNT",
        "Emerita Resources Corp.": "EMO",
        "Emergent Metals Corp.": "EMR",
        "EMX Royalty Corporation": "EMX",
        "Entourage Health Corp.": "ENTG",
        "Eco (Atlantic) Oil & Gas Ltd.": "EOG",
        "EQ Inc.": "EQ",
        "Equity Metals Corporation": "EQTY",
        "Eros Resources Corp.": "ERC",
        "ESE Entertainment Inc.": "ESE",
        "Esstra Industries Inc.": "ESS",
        "Encore Energy Corp.": "EU",
        "Evergold Corp.": "EVER",
        "EverGen Infrastructure Corp.": "EVGN",
        "Evome Medical Technologies Inc.": "EVMT",
        "European Electric Metals Inc.": "EVX",
        "East West Petroleum Corp": "EW",
        "Earthworks Industries Inc.": "EWK",
        "Environmental Waste International Inc.": "EWS",
        "ExGen Resources Inc.": "EXG",
        "Fountain Asset Corp.": "FA",
        "Fairchild Gold Corp.": "FAIR",
        "First Atlantic Nickel Corp.": "FAN",
        "Deveron Corp.": "FARM",
        "First Andes Silver Ltd.": "FAS",
        "Fjordland Exploration Inc.": "FEX",
        "Falcon Gold Corp.": "FG",
        "Frontier Lithium Inc.": "FL",
        "Forum Energy Metals Corp.": "FMC",
        "Fidelity Minerals Corp.": "FMN",
        "Focus Graphite Inc.": "FMS",
        "Fortune Bay Corp.": "FOR",
        "FPX Nickel Corp.": "FPX",
        "Freeport Resources Inc.": "FRI",
        "The Fresh Factory B.C. Ltd": "FRSH",
        "Fintech Select Ltd.": "FTEC",
        "FTI Foodtech International Inc.": "FTI",
        "Katipult Technology Corp.": "FUND",
        "Gabo Mining Ltd.": "GAB",
        "Galantas Gold Corporation": "GAL",
        "Goldex Resources Corporation": "GDX",
        "Graphano Energy Ltd.": "GEL",
        "Green Battery Minerals Inc.": "GEM",
        "Generation Uranium Inc.": "GEN",
        "Genius Metals Inc.": "GENI",
        "Genix Pharmaceuticals Corporation": "GENX",
        "G6 Materials Corp.": "GGG",
        "Granada Gold Mine Inc.": "GGM",
        "Giga Metals Corporation": "GIGA",
        "ReGen III Corp.": "GIII",
        "Gladiator Metals Corp.": "GLAD",
        "GoldON Resources Ltd.": "GLD",
        "Good Gamer Entertainment Inc.": "GOOD",
        "Great Pacific Gold Corp.": "GPAC",
        "Green Rise Foods Inc.": "GRF",
        "Galore Resources Inc": "GRI",
        "GT Resources Inc.": "GT",
        "Gungnir Resources Inc.": "GUG",
        "Hawkeye Gold & Diamond Inc.": "HAWK",
        "Hempalta Corp.": "HEMP",
        "Helius Minerals Limited": "HHH",
        "Highland Copper Company Inc.": "HI",
        "Highgold Mining Inc.": "HIGH",
        "High Tide Inc.": "HITI",
        "HIVE Digital Technologies Ltd.": "HIVE",
        "HPQ Silicon Inc.": "HPQ",
        "Imperial Equities Inc.": "IEI",
        "Inspire Semiconductor Holdings Inc.": "INSP",
        "Intrepid Metals Corp.": "INTR",
        "Lithium ION Energy Ltd.": "ION",
        "Innovotech Inc.": "IOT",
        "AirIQ Inc": "IQ",
        "Jade Leader Corp.": "JADE",
        "Japan Gold Corp.": "JG",
        "Kalo Gold Corp.": "KALO",
        "Kutcho Copper Corp.": "KC",
        "Kestrel Gold Inc.": "KGC",
        "Kingman Minerals Ltd.": "KGS",
        "Kenorland Minerals Ltd.": "KLD",
        "Kingsmen Resources Ltd.": "KNG",
        "Kore Mining Ltd.": "KORE",
        "Klondike Silver Corp.": "KS",
        "Kootenay Silver Inc.": "KTN",
        "KWESST Micro Systems Inc.": "KWE",
        "Labrador Gold Corp.": "LAB",
        "Lion Copper and Gold Corp.": "LEO",
        "Lithium Energi Exploration Inc.": "LEXI",
        "Lifeist Wellness Inc.": "LFST",
        "American Lithium Corp.": "LI",
        "Argentina Lithium & Energy Corp.": "LIT",
        "Lithium Chile Inc.": "LITH",
        "Canada Rare Earth Corp.": "LL",
        "TomaGold Corporation": "LOT",
        "Cannara Biotech Inc.": "LOVE",
        "Lodestar Battery Metals Corp.": "LSTR",
        "Lithium Ionic Corp.": "LTH",
        "Themac Resources Group Limited": "MAC",
        "ProStar Holdings Inc.": "MAPS",
        "Mas Gold Corp.": "MAS",
        "Masivo Silver Corp.": "MASS",
        "MAX Resource Corp.": "MAX",
        "Minnova Corp.": "MCI",
        "McChip Resources Inc": "MCS",
        "Midland Exploration Inc": "MD",
        "Midwest Energy Emissions Corp.": "MEEC",
        "Metal Energy Corp.": "MERG",
        "Metalore Resources Limited": "MET",
        "Mayfair Gold Corp.": "MFG",
        "Maple Gold Mines Ltd.": "MGM",
        "MustGrow Biologics Corp.": "MGRO",
        "Mineral Hill Industries Ltd.": "MHI",
        "Inomin Mines Inc.": "MINE",
        "MedMira Inc.": "MIR",
        "Millennial Potash Corp.": "MLP",
        "Midnight Sun Mining Corp": "MMA",
        "Minco Capital Corp.": "MMM",
        "Macarthur Minerals Limited": "MMS",
        "Moon River Moly Ltd.": "MOO",
        "Blue Moon Metals Inc.": "MOON",
        "Marvel Biosciences Corp.": "MRVL",
        "Millennium Silver Corp.": "MSC",
        "M3 Metals Corp.": "MT",
        "Metalla Royalty & Streaming Ltd.": "MTA",
        "MTB Metals Corp.": "MTB",
        "Mammoth Resources Corp.": "MTH",
        "Metallis Resources Inc.": "MTS",
        "Metalex Ventures Ltd": "MTX",
        "Murchison Minerals Ltd.": "MUR",
        "Nubian Resources Ltd": "NBR",
        "Niobay Metals Inc.": "NBY",
        "NTG Clarity Networks Inc.": "NCI",
        "New Found Gold Corp.": "NFG",
        "Nickelex Resource Corporation": "NICK",
        "Nicola Mining Inc.": "NIM",
        "Nio Strategic Metals Inc.": "NIO",
        "Northern Lion Gold Corp.": "NL",
        "Namibia Critical Metals Inc.": "NMI",
        "NowVertical Group Inc.": "NOW",
        "Neupath Health Inc.": "NPTH",
        "New Tymbal Resources Ltd.": "NTB",
        "Nortec Minerals Corp.": "NVT",
        "NV Gold Corporation": "NVX",
        "NexgenRx Inc.": "NXG",
        "Olive Resource Capital Inc.": "OC",
        "Outcrop Silver & Gold Corporation": "OCG",
        "Odd Burger Corporation": "ODD",
        "Osisko Development Corp.": "ODV",
        "Orogen Royalties Inc.": "OGN",
        "Osisko Metals Incorporated": "OM",
        "Orosur Mining Inc.": "OMI",
        "Onyx Gold Corp.": "ONYX",
        "Oracle Commodity Holding Corp.": "ORCL",
        "OneSoft Solutions Inc.": "OSS",
        "Oculus VisionTech Inc.": "OVT",
        "Outback Goldfields Corp.": "OZ",
        "Palisades Goldcorp Ltd.": "PALI",
        "Pacific Bay Minerals Ltd.": "PBM",
        "Petrolympic Ltd": "PCQ",
        "Pegasus Resources Inc.": "PEGA",
        "Pacific Empire Minerals Corp.": "PEMC",
        "Pacific Ridge Exploration Ltd.": "PEX",
        "PetroFrontier Corp": "PFC",
        "Plato Gold Corp.": "PGC",
        "Power Group Projects Corp.": "PGP",
        "Prosper Gold Corp.": "PGX",
        "Pan Global Resources Inc.": "PGZ",
        "Providence Gold Mines Inc.": "PHD",
        "Perimeter Medical Imaging AI, Inc.": "PINK",
        "Plurilock Security Inc.": "PLUR",
        "Panoro Minerals Ltd.": "PML",
        "ProAm Explorations Corporation": "PMX",
        "Pool Safe Inc.": "POOL",
        "Portofino Resources Inc.": "POR",
        "Precipitate Gold Corp.": "PRG",
        "Pearl River Holdings Limited": "PRH",
        "Petrox Resources Corp.": "PTC",
        "Principal Technologies Inc.": "PTEC",
        "Pender Growth Fund Inc.": "PTF",
        "Proton Capital Corp.": "PTN",
        "Power Metals Corp.": "PWM",
        "Pelangio Exploration Inc.": "PX",
        "Quorum Information Technologies Inc.": "QIS",
        "Q2 Metals Corp.": "QTWO",
        "Ramp Metals Inc.": "RAMP",
        "Tactical Resources Corp.": "RARE",
        "E-Tech Resources Inc.": "REE",
        "Regulus Resources Inc.": "REG",
        "Auric Resources Corp.": "RES",
        "Orex Minerals Inc.": "REX",
        "Relevant Gold Corp.": "RGC",
        "Reco International Group Inc.": "RGI",
        "Rio2 Limited": "RIO",
        "Richmond Minerals Inc.": "RMD",
        "Ridgestone Mining Inc.": "RMI",
        "Rome Resources Ltd.": "RMR",
        "Rockridge Resources Ltd.": "ROCK",
        "ROK Resources Inc.": "ROK",
        "Northstar Clean Technologies Inc.": "ROOF",
        "Rathdowney Resources Ltd.": "RTH",
        "RT Minerals Corp.": "RTM",
        "Rocky Mountain Liquor Inc.": "RUM",
        "Rhyolite Resources Ltd": "RYE",
        "Sage Potash Corp.": "SAGE",
        "Asian Television Network International Ltd.": "SAT",
        "SATO Technologies Corp.": "SATO",
        "Sparta Capital Ltd.": "SAY",
        "Sabio Holdings Inc.": "SBIO",
        "Scandium Canada Ltd.": "SCD",
        "Santacruz Silver Mining Ltd.": "SCZ",
        "Spectra7 Microsystems Inc.": "SEV",
        "Solstice Gold Corp.": "SGC",
        "Snowline Gold Corp.": "SGD",
        "Strategem Capital Corporation": "SGE",
        "Sigma Lithium Corporation": "SGML",
        "Scorpio Gold Corporation": "SGN",
        "Signature Resources Ltd.": "SGU",
        "Sitka Gold Corp.": "SIG",
        "Silver Valley Metals Corp.": "SILV",
        "San Lorenzo Gold Corp.": "SLG",
        "Standard Lithium Ltd.": "SLI",
        "Sierra Madre Gold and Silver Ltd.": "SM",
        "Sun Summit Minerals Corp.": "SMN",
        "Southern Empire Resources Corp.": "SMP",
        "Sonoro Energy Ltd.": "SNV",
        "Sirios Resources Inc.": "SOI",
        "Solar Alliance Energy Inc.": "SOLR",
        "SPC Nickel Corp.": "SPC",
        "Silver Predator Corp.": "SPD",
        "Canadian Spirit Resources Inc.": "SPI",
        "South Pacific Metals Corp.": "SPMC",
        "EarthLabs Inc.": "SPOT",
        "Strategic Resources Inc.": "SR",
        "Saville Resources Inc.": "SRE",
        "SRG Mining Inc.": "SRG",
        "Sparton Resources Inc.": "SRI",
        "Salazar Resources Limited": "SRL",
        "Starr Peak Mining Ltd.": "STE",
        "Stinger Resources Inc.": "STNG",
        "Storm Exploration Inc.": "STRM",
        "Star Royalties Ltd.": "STRR",
        "Superior Mining International Corporation": "SUI",
        "Northern Superior Resources Inc.": "SUP",
        "Surge Copper Corp.": "SURG",
        "Black Swan Graphene Inc.": "SWAN",
        "Tombill Mines Limited": "TBLL",
        "Turmalina Metals Corp.": "TBX",
        "TDG Gold Corp.": "TDG",
        "Telo Genomics Corp.": "TELO",
        "Trifecta Gold Ltd.": "TG",
        "Thunder Mountain Gold, Inc.": "THM",
        "Therma Bright Inc.": "THRM",
        "Till Capital Corporation": "TIL",
        "Tiny Ltd.": "TINY",
        "Tinka Resources Limited": "TK",
        "Theralase Technologies Inc.": "TLT",
        "Trigon Metals Inc.": "TM",
        "Trench Metals Corp.": "TMC",
        "Torr Metals Inc.": "TMET",
        "Topicus.com Inc.": "TOI",
        "Pucara Gold Ltd.": "TORO",
        "Tenth Avenue Petroleum Corp.": "TPC",
        "Tethys Petroleum Limited": "TPL",
        "Troubadour Resources Inc.": "TR",
        "Tres-Or Resources Ltd.": "TRS",
        "TRU Precious Metals Corp.": "TRU",
        "Thiogenesis Therapeutics, Corp.": "TTI",
        "T2 Metals Corp.": "TWO",
        "UGE International Ltd.": "UGE",
        "Vatic Ventures Corp": "VCV",
        "Visionstate Corp.": "VIS",
        "Volt Lithium Corp.": "VLT",
        "Vicinity Motor Corp.": "VMC",
        "Valore Metals Corp.": "VO",
        "VVC Exploration Corporation": "VVC",
        "Valleyview Resources Ltd.": "VVR",
        "Vizsla Silver Corp.": "VZLA",
        "Waverley Pharma Inc.": "WAVE",
        "Western Exploration Inc.": "WEX",
        "White Gold Corp.": "WGO",
        "Wishpond Technologies Ltd.": "WISH",
        "Whitemud Resources Inc": "WMK",
        "Western Metallica Resources Corp.": "WMS",
        "Grey Wolf Animal Health Corp.": "WOLF",
        "XORTX Therapeutics Inc.": "XRTX"
    }
    
    periods = {
        "1 semaine": timedelta(weeks=1),
        "2 mois": timedelta(days=60),
        "6 mois": timedelta(days=182),
        "1 an": timedelta(days=365),
        "3 ans": timedelta(days=3*365),
        "5 ans": timedelta(days=5*365)
    }

    results = []

    for name, symbol in companies.items():
        row = [name, symbol]
        for label, period in periods.items():
            data = get_stock_data(symbol, period)
            if not data.empty:
                progression = calculate_progression(data, period)
                row.append(progression)
            else:
                row.append(None)
        results.append(row)
    
    headers = ["Nom de la société", "Symbole"] + list(periods.keys())
    df = pd.DataFrame(results, columns=headers)
    
    # Sort the DataFrame by the '5 ans' column in descending order
    df = df.sort_values(by="5 ans", ascending=False, na_position='last')
    
    # Format the percentage columns as strings with "%" symbol
    for col in periods.keys():
        df[col] = df[col].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "Données non disponibles")
    
    # Save the DataFrame to a CSV file with ';' as the separator
    output_path = "canadian_stocks_progression.csv"  # Adjust this path to a valid location on your system
    df.to_csv(output_path, sep=';', index=False)

    return df

# Run the main function and display the dataframe
df = main()
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))