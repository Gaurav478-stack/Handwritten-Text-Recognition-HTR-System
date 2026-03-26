import math
from pathlib import Path


def run_scientific_job() -> str:
    """Compute sample scientific values and write them to /app/output/results.txt."""
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    values = {
        "pi": math.pi,
        "exp_1": math.e,
        "sqrt_2": math.sqrt(2),
        "sin_45": math.sin(math.radians(45)),
        "log_10": math.log(10),
    }

    lines = ["Scientific Job Results", "=" * 24]
    for key, value in values.items():
        lines.append(f"{key}: {value:.8f}")

    output_file = output_dir / "results.txt"
    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(output_file)


if __name__ == "__main__":
    result_path = run_scientific_job()
    print(f"Job completed. Output written to: {result_path}")
