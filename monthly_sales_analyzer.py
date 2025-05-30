# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total_sales = 0
    for i in data:
        if product_key:
            total_sales += i[product_key]
    return total_sales
    

# print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))

def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total = 0
    for i in data:
        total += i[product_key]
    average = total / len(data)
    return average

# print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))

def best_selling_day(data):
    """Finds the day with the highest total sales."""
    max_int = 0
    resultado = {}
    for i in data:
        day = i["day"]
        total = i["product_a"]+i["product_b"]+i["product_c"]

        if total > max_int:
            max_int = total
            resultado = {"day":day, "total_sales":total}
    return resultado


#print("Day with highest total sales:", best_selling_day(sales_data))


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    upper_threshold = 0
    for i in data:
        if i[product_key]>threshold:
            upper_threshold += 1
    return upper_threshold

#print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))

def top_product(data):
    """Determines which product had the highest total sales in 30 days."""

    total_sales = {"product_a": 0, "product_b": 0, "product_c": 0}

    for i in data:
        total_sales["product_a"] += i["product_a"]
        total_sales["product_b"] += i["product_b"]
        total_sales["product_c"] += i["product_c"]

    if total_sales["product_a"] >= total_sales["product_b"] and total_sales["product_a"] >= total_sales["product_c"]:
        top_product = "product_a"
    elif total_sales["product_b"] >= total_sales["product_c"]:
        top_product= "product_b"
    else:
        top_product= "product_c"

    return top_product

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))

#Agrega una función para encontrar el día con las peores ventas.

def worst_selling_day(data):
    """Finds the day with the highest total sales."""
    min_int = float('inf')
    resultado = {}
    for i in data:
        day = i["day"]
        total = i["product_a"]+i["product_b"]+i["product_c"]

        if total < min_int:
            min_int = total
            resultado = {"day":day, "total_sales":total}
    return resultado

print("Day with lowest total sales:", worst_selling_day(sales_data))

#Ordena los días por ventas totales y muestra los 3 mejores.
def best_selling_days(data):
    for i in data:
        i["total_sales"] = i["product_a"] + i["product_b"] + i["product_c"]

    data.sort(key = lambda x: x["total_sales"], reverse=True)
    return sales_data[:3]

print("Days with highest total sales:", best_selling_days(sales_data))    

#Calcula el rango (máximo - mínimo) de las ventas de un producto.
def sales_ranges(product_key, sales_data):
    sales = [day[product_key] for day in sales_data]
    max_range = max(sales) - min(sales)
    min_range = None
    
    for i in range(1, len(sales)):
        current = sales[i]
        previous = sales[i - 1]

        if current > previous:
            difference = current - previous
        else:
            difference = previous - current

        if difference != 0:
            if min_range is None or difference < min_range:
                min_range = difference

    return {
        "product": product_key,
        "max_range": max_range,
        "min_range": min_range
    }

for product in ["product_a", "product_b", "product_c"]:
    result = sales_ranges(product, sales_data)
    print(f"{product}: Maximum Range = {result['max_range']}, Minimum Range = {result['min_range']}")
