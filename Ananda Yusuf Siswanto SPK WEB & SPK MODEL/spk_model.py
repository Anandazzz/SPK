from settings import MEREK_SCALE,DEV_SCALE_ram,DEV_SCALE_prosesor,DEV_SCALE_storage,DEV_SCALE_baterai,DEV_SCALE_harga,DEV_SCALE_webcam

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            'brand': 5, 
            'ram': 3, 
            'prosesor': 4, 
            'storage': 3, 
            'baterai': 4, 
            'harga': 3, 
            'webcam': 1
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]] # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]] # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': laptop['id'],
            'brand': MEREK_SCALE[laptop['brand']],
            'ram': DEV_SCALE_ram[laptop['ram']],
            'prosesor': DEV_SCALE_prosesor[laptop['prosesor']],
            'storage': DEV_SCALE_storage[laptop['storage']],
            'baterai': DEV_SCALE_baterai[laptop['baterai']],
            'harga': DEV_SCALE_harga[laptop['harga']],
            'webcam': DEV_SCALE_webcam[laptop['webcam']]
        } for laptop in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brand = [] # max
        ram = [] # max
        prosesor = [] # max
        storage = [] # max
        baterai = [] # max
        harga = [] # min
        webcam = [] # max
        for data in self.data:
            brand.append(data['brand'])
            ram.append(data['ram'])
            prosesor.append(data['prosesor'])
            storage.append(data['storage'])
            baterai.append(data['baterai'])
            harga.append(data['harga'])
            webcam.append(data['webcam'])

        max_brand = max(brand)
        max_ram = max(ram)
        max_prosesor = max(prosesor)
        max_storage = max(storage)
        max_baterai = max(baterai)
        min_harga = min(harga)
        max_webcam = max(webcam)

        return [
            {   'id': data['id'],
                'brand': data['brand']/max_brand, # benefit
                'ram': data['ram']/max_ram, # benefit
                'prosesor': data['prosesor']/max_prosesor, # benefit
                'storage': data['storage']/max_storage, # benefit
                'baterai': data['baterai']/max_baterai, # benefit
                'harga': min_harga/data['harga'], # cost
                'webcam': data['webcam']/max_webcam # benefit
                }
            for data in self.data
        ]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['brand'] ** weight['brand'] *
        row['ram'] ** weight['ram'] *
        row['prosesor'] ** weight['prosesor'] *
        row['storage'] ** weight['storage'] *
        row['baterai'] ** weight['baterai'] *
        row['harga'] ** weight['harga'] *
        row['webcam'] ** (-weight['webcam']) 
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))