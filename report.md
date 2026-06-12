# SoilSense — Smart Soil Analysis System

**Course:** Python Programming

**Senior Project:** (Smart Soil Inspection System)

## Members

* Tamara Yousef Hamarsheh — 202110370 — Responsible for: soil_analyzer.py, create_sample_data.py
* Jamila Jamal Daraghmeh — 202010358 — Responsible for: visualizer.py, main.py, requirements.txt

**GitHub Repository:**https://github.com/tamarayousef778-lang/SoilSense_Hamarsheh_Daraghmeh.git

---

# 2. Project Description

SoilSense is a Smart Soil Analysis System, which analyses soil data and determines soil health condition. The system imports soil data from a CSV file, analyzes soil pH, soil moisture, soil nitrogen content, soil phosphorus content, and soil potassium content, and scores soil health based on that information. Then, depending on the soil health score calculated by the system, soil health condition is determined to be Excellent, Good, Fair, or Poor. Moreover, the system provides suggestions for improvement of soil condition, in terms of applying fertilizers and irrigation to the soil. Matplotlib library is used to visualize the dashboard and the charts for users' better understanding of their soils' health condition.

---

# 3. Libraries Used

| Library    | Version  | How it was used                                    |
| ---------- | -------- | -------------------------------------------------- |
| numpy      | 2.4.6    | Score calculations, statistics, and range clipping |
| matplotlib | 3.10.9    | Nutrient chart, pH indicator, and health dashboard |
| csv        | Built-in | Reading soil data from CSV files                   |
| json       | Built-in | Saving analysis reports in JSON format             |

---

# 4. Module Descriptions

## soil_analyzer.py

The task of loading the data on soils, score calculation, soil health classification, and recommendation generation is handled by the SoilAnalyzer class. The most critical function is the analyze_all() function since it encapsulates everything else done by the other methods.

## visualizer.py

Charts and dashboards are produced by the Visualizer class, which contain information related to soil health. The key function here is health_dashboard(), which generates an overview of all scores and classifications using bar charts and pie charts.

## main.py

Main.py is responsible for acting as the controller in the application. Main.py loads the soil data, carries out the analysis, writes the report to json, and shows all the visualization plots. 

---

# 5. Test Cases

## Test 1: load_samples()

**Input:** soil_readings.csv

**Expected Output:** 6 soil samples loaded successfully with correct data types.

**Actual Output:** 6 samples loaded successfully. 

### Code Used

```python
analyzer = SoilAnalyzer()
samples = analyzer.load_samples("soil_readings.csv")

print(len(samples))
print(type(samples[0]["sample_id"]))
print(type(samples[0]["ph"]))
```

---

## Test 2: classify_sample()

**Input:** Various score values

**Expected Output:**

* 95 → Excellent
* 75 → Good
* 55 → Fair
* 30 → Poor

**Actual Output:** All classifications returned correctly. 

### Code Used

```python
analyzer = SoilAnalyzer()

print(analyzer.classify_sample(95.0))
print(analyzer.classify_sample(75.0))
print(analyzer.classify_sample(55.0))
print(analyzer.classify_sample(30.0))
```

---

## Test 3: get_recommendations()

**Input:** Sample with low pH, low moisture, and low nutrients.

**Expected Output:** Multiple recommendations for pH correction, irrigation, and fertilizers.

**Actual Output:** All expected recommendations were generated. 

### Code Used

```python
sample = {
    "ph": 4.5,
    "moisture": 20,
    "nitrogen": 10,
    "phosphorus": 5,
    "potassium": 60
}

analyzer = SoilAnalyzer()

for recommendation in analyzer.get_recommendations(sample):
    print(recommendation)
```

---

## Test 4: Full Application Run

**Input:** python main.py

**Expected Output:**

* Analysis completes successfully
* Dashboard appears
* Nutrient chart appears
* pH indicator appears
* JSON report is created

**Actual Output:** Application executed successfully with all charts displayed. 

---

# 6. Screenshots

## Health Dashboard

![Dashboard](screenshots/health_dashboard.png)

*Score bar chart and classification pie chart for all samples*

---

## Nutrient Chart

![Nutrients](screenshots/nutrient_chart.png)

*Nutrient levels as percentage of ideal for one sample*

---

## pH Indicator

![pH](screenshots/ph_indicator.png)

*Color-coded pH scale with current value marked*

---

## Terminal Output

![Terminal](screenshots/terminal_output.png)

*Full output of running python main.py*

---

# 7. Individual Contributions

| Student                 | ID        | Files                                    | Commit Count| GitHub Username        |
| ----------------------- | --------- | ---------------------------------------- | ------------| ---------------        |
| Tamara Yousef Hamarsheh | 202110370 | soil_analyzer.py, create_sample_data.py  | ?           | @tamarayousef778-lang  |
| Jamila Jamal Daraghmeh  | 202010358 | visualizer.py, main.py, requirements.txt | ?           |@jamiladaraghmeh123     |

---

# 8. Challenges & What We Learned

### Tamara Yousef Hamarsheh (202110370)

The first problem was related to the development of the scoring algorithm for soil parameters without exceeding the necessary score limit. It was resolved through using NumPy clipping techniques and experimenting with various parameter values to test the formula.

### Jamila Jamal Daraghmeh (202010358)

One difficulty was the design of informative and well-presented visuals using Matplotlib. This was overcome by utilizing various graphs and colors to convey the classification and nutrient information properly.

### Connection to the Senior Project

The present analysis program written in Python language is the software component of the Smart Soil Inspection System. In the whole project to be conducted by the seniors, the measurements obtained by the sensors attached to the soil shall be transferred to the application and analyzed by the algorithms provided here.

---

# 9. How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

Generated using:

```bash
pip freeze > requirements.txt
```

## Create Sample Soil Data

```bash
python create_sample_data.py
```

## Run the Analysis

```bash
python main.py
```
