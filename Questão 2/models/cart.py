class Cart:
    def __init__(self):
        self.products = []
        
    def add_product(self, product, qtd=1):
        for item in self.products:
            if item['product'] == product:
                item['qtd'] += qtd
                return
        self.products.append({'product': product, 'qtd': qtd})
        
    def remove_product(self, product, qtd=1):
        for item in self.products:
            if item['product'] == product:
                if item['qtd'] <= qtd:
                    self.products.remove(item)
                else:
                    item['qtd'] -= qtd
                return
            
    def calculate_total(self):
        total = 0
        for item in self.products:
            total += item['product'].price * item['qtd']
        return total
    
    def finalize_order(self):
        pass
    