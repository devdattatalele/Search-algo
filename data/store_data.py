STORE_HIERARCHY = {
    "Electronics": {
        "Smartphones": ["Samsung Galaxy", "Apple iPhone", "Google Pixel", "OnePlus", "Xiaomi Redmi"],
        "Laptops": ["Dell XPS", "HP Spectre", "Apple MacBook", "Lenovo ThinkPad"],
        "Headphones": ["Sony WH-1000XM5", "Bose QC45", "Jabra Elite", "Sennheiser HD 450BT"]
    },
    "Apparel": {
        "Footwear": ["Nike Air Max", "Adidas UltraBoost", "Puma Suede", "New Balance 990"],
        "Outerwear": ["Columbia Jacket", "The North Face Parka", "Patagonia Fleece", "Arc'teryx Shell"],
        "Jeans": ["Levi's 501", "Wrangler Relaxed", "Lee Straight", "Diesel Slim"]
    },
    "Home Goods": {
        "Kitchen Appliances": ["Instant Pot", "KitchenAid Mixer", "Ninja Blender", "Cuisinart Toaster"],
        "Furniture": ["IKEA Sofa", "Ashley Table", "West Elm Chair", "Pottery Barn Bed"],
        "Bedding": ["Brooklinen Sheets", "Parachute Duvet", "Casper Mattress", "Tuft & Needle Pillow"]
    },
    "Perfumes": {
        "Designer Fragrances": ["Dior Sauvage", "Chanel No. 5", "Versace Dylan Blue", "Gucci Bloom", "Yves Saint Laurent Y"],
        "Niche Perfumes": ["Creed Aventus", "Tom Ford Tobacco Vanille", "Jo Malone Wood Sage & Sea Salt", "Byredo Mojave Ghost"]
    }
}

def get_all_brands():
    brands = []
    for category_data in STORE_HIERARCHY.values():
        for product_type_data in category_data.values():
            brands.extend(product_type_data)
    return brands

def build_graph_from_hierarchy(hierarchy):
    graph = {}
    root_node = "Department Store"
    graph[root_node] = []
    for category, products in hierarchy.items():
        graph[root_node].append(category)
        if category not in graph:
            graph[category] = []
        for product_type, brands in products.items():
            graph[category].append(product_type)
            if product_type not in graph:
                graph[product_type] = []
            for brand in brands:
                graph[product_type].append(brand)
                if brand not in graph:
                    graph[brand] = []
    return graph 