import json
from soil_analyzer import SoilAnalyzer
from visualizer import Visualizer


def main():
    DATA_FILE = "soil_readings.csv"
    REPORT_FILE = "soil_report.json"

    analyzer = SoilAnalyzer()
    viz = Visualizer()

    print("[1/4] Loading soil samples...")
    samples = analyzer.load_samples(DATA_FILE)
    print(f"Loaded {len(samples)} samples\n")

    print("[2/4] Analyzing soil health...")
    results = analyzer.analyze_all(samples)

    print("\n=== Per-Sample Results ===")

    for sample in results:
        print(f"\n[{sample['sample_id']}] {sample['location']}")
        print(f"Score: {sample['total_score']}/100")
        print(f"Classification: {sample['classification']}")
        print("Recommendations:")

        for rec in sample["recommendations"]:
            print(f"- {rec}")
        print("\n[3/4] Saving report...")

    with open(REPORT_FILE, "w") as file:
        json.dump(results, file, indent=2)

    print(f"Report saved: {REPORT_FILE}")

    print("[4/4] Displaying visualizations...")
    viz.health_dashboard(results)

    for sample in results[:2]:
        viz.nutrient_chart(sample)
        viz.ph_indicator(sample)

    print("\nDone!")


if __name__ == "__main__":
    main()
    