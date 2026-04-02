import json
from pathlib import Path
from src.workflow import run_workflow
from src.logger import save_result

def load_products():
    path = Path("data/sample_products.json")
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    products = load_products()
    product = products[0]

    result = run_workflow(product)
    save_result(product["product_name"], result)

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()