
# From Desert 2 Oasis

## Overview
**From Desert 2 Oasis** is a comprehensive initiative aimed at addressing food deserts and improving access to healthy food options through geospatial technology. Within this initiative, **Project Radius** focuses on leveraging advanced spatial data science and geospatial algorithms to recommend strategic locations for new grocery stores in underserved areas.

---

## About Project Radius
**Project Radius** is a deep-dive into the capabilities of **ArcGIS Pro** and the **ArcGIS Python Library (arcpy)**, exploring their potential for geospatial analysis and algorithmic decision-making. This project focuses on using data-driven insights and actionable recommendations to improve food access in underserved areas.

### Objective
Recommend optimal locations for new grocery stores in **Rochester**, addressing the needs of residents living in food deserts. The project's goal is to visualize the current landscape of healthy and unhealthy food options and implement a custom algorithm to suggest new grocery store locations that improve food access.

---

## Methodology

### Tools and Data
- **ArcGIS Pro / Online**: For mapping and visualization.
- **Google Maps API**: To gather location data for existing food options.
- **ArcGIS arcpy Python Library**: To implement spatial algorithms and automate data processing.
- **VSCode**: For Python script development.

### Workflow
1. **Data Collection**:
   - Gather geographic coordinates for:
     - Healthy grocery stores.
     - Corner stores and fast-food restaurants (unhealthy food options).
   - Compile these locations into a feature layer in ArcGIS.

2. **Mapping**:
   - Plot points for all food options, color-coded to distinguish between healthy and unhealthy options.
   - Visualize a two-mile radius around each point to represent their service area.

3. **Algorithm Development**:
   - Develop and implement a custom spatial algorithm to analyze the feature layer.
   - The algorithm will:
     - Identify underserved areas lacking healthy grocery options within a two-mile radius.
     - Recommend new grocery store locations based on the spatial analysis.

4. **Visualization**:
   - Generate an updated feature layer with the proposed grocery store locations.
   - Use visual overlays to highlight the new grocery store points and their service areas, effectively reducing the food deserts in Rochester.

5. **Output**:
   - Produce a final map displaying the revised food landscape of Rochester, emphasizing improved access to healthy food options.

---

## Expected Outcome
The output of **Project Radius** will be a data-driven map that identifies and fills gaps in grocery store coverage within Rochester. By applying advanced geospatial analysis, the project will provide actionable recommendations to mitigate food deserts and enhance food equity.

---

## Next Steps
- Finalize and refine the algorithm to ensure intentional placement of new grocery store locations.
- Test and validate the results with sample data.
- Explore additional layers of analysis, such as population density or socioeconomic factors, to enhance the accuracy and relevance of the recommendations.

---

**From Desert 2 Oasis - Project Radius** demonstrates the power of spatial data science to address real-world challenges, paving the way for more equitable access to essential resources.

---

Let me know if you need any further changes!