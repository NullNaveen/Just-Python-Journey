# Rechecking and restructuring the roadmap processing logic
# Create the Excel writer again
file_path = r"C:\Users\Nike\Documents\Programming\Python\Chat GPT codes\Data_Science_Learning_Roadmap.xlsx"
writer = pd.ExcelWriter(file_path, engine="xlsxwriter")

# Correctly process and write each skill to separate sheets
for skill, content in data_science_roadmap.items():
    rows = []
    if isinstance(content, dict) and "topics" in content:  # Single-layer skill handling
        rows.extend([
            (topic, time, "", content["sources"][0] if content["sources"] else "")
            for topic, time in zip(content["topics"], content["time"])
        ])
    else:  # Multi-layer skill handling
        for sub_skill, sub_content in content.items():
            rows.extend([
                (f"{sub_skill} - {topic}", time, "", sub_content["sources"][0] if sub_content["sources"] else "")
                for topic, time in zip(sub_content["topics"], sub_content["time"])
            ])

    # Create DataFrame for the skill
    df = pd.DataFrame(rows, columns=["Skill/Topic", "Estimated Time (weeks)", "Status", "Source"])
    # Write the DataFrame to an Excel sheet
    df.to_excel(writer, sheet_name=skill[:31], index=False)  # Excel sheet names are limited to 31 characters

# Save the Excel file
writer.close()
file_path
