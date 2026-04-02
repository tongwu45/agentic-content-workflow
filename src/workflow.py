import json
from src.llm import call_llm_json
from src.utils import load_text

def run_workflow(product: dict) -> dict:
    strategist_prompt = load_text("prompts/strategist.txt")
    generator_prompt = load_text("prompts/generator.txt")
    critic_prompt = load_text("prompts/critic.txt")
    refiner_prompt = load_text("prompts/refiner.txt")
    adapter_prompt = load_text("prompts/adapter.txt")

    product_json = json.dumps(product, indent=2, ensure_ascii=False)

    strategy = call_llm_json(
        strategist_prompt,
        f"Analyze this product input:\n{product_json}"
    )

    draft = call_llm_json(
        generator_prompt,
        f"Product:\n{product_json}\n\nStrategy:\n{json.dumps(strategy, indent=2, ensure_ascii=False)}"
    )

    critique = call_llm_json(
        critic_prompt,
        f"Product:\n{product_json}\n\nDraft:\n{json.dumps(draft, indent=2, ensure_ascii=False)}"
    )

    refined = call_llm_json(
        refiner_prompt,
        f"Product:\n{product_json}\n\nDraft:\n{json.dumps(draft, indent=2, ensure_ascii=False)}\n\nCritique:\n{json.dumps(critique, indent=2, ensure_ascii=False)}"
    )

    adapted = call_llm_json(
        adapter_prompt,
        f"Product:\n{product_json}\n\nRefined:\n{json.dumps(refined, indent=2, ensure_ascii=False)}"
    )

    return {
        "strategy": strategy,
        "draft": draft,
        "critique": critique,
        "refined": refined,
        "adapted": adapted,
    }