import json
from soil_analyzer import SoilAnalyzer
from visualizer import Visualizer


def main():
    DATA_FILE = "soil_readings.csv"
    REPORT_FILE = "soil_report.json"

    analyzer = SoilAnalyzer()
    viz = Visualizer()