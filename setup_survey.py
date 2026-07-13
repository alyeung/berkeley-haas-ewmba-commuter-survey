import urllib.request
import json
import time
import os

# Configuration: Read API credentials from environment variables to prevent exposure
API_TOKEN = os.environ.get("QUALTRICS_API_TOKEN", "YOUR_API_TOKEN_HERE")
DATA_CENTER = os.environ.get("QUALTRICS_DATA_CENTER", "yul1") # e.g. 'yul1', 'ca1', 'us1'
BASE_URL = f"https://{DATA_CENTER}.qualtrics.com/API/v3"

def make_request(url, method="GET", payload=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("X-API-TOKEN", API_TOKEN)
    req.add_header("Content-Type", "application/json")
    
    data_bytes = None
    if payload is not None:
        data_bytes = json.dumps(payload).encode('utf-8')
        
    try:
        with urllib.request.urlopen(req, data=data_bytes) as response:
            return response.status, json.loads(response.read().decode('utf-8'))
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, "read"):
            error_msg = e.read().decode('utf-8')
        return 400, {"error": error_msg}

# 1. Create survey
print("Creating survey...")
survey_payload = {
    "SurveyName": "Haas Evening and Weekend MBA Commuter Survey",
    "Language": "EN",
    "ProjectCategory": "CORE"
}
status, resp = make_request(f"{BASE_URL}/survey-definitions", "POST", survey_payload)
if status != 200:
    print(f"Failed to create survey: {resp}")
    exit(1)

survey_id = resp["result"]["SurveyID"]
block_id = resp["result"]["DefaultBlockID"]
print(f"Survey created successfully!")
print(f"Survey ID: {survey_id}")
print(f"Block ID: {block_id}\n")

# 2. Define questions
questions = [
    {
        "QuestionText": "<b>Haas Evening & Weekend MBA (EWMBA) Commuter Survey</b><br><br>Help us advocate for better commuting and parking options at Haas. This 3-minute survey is conducted by your Evening & Weekend MBA Association (EWMBAA) officers. Your responses are completely anonymous, confidential, and will be shared directly with Haas leadership.",
        "QuestionType": "DB",
        "Selector": "TB"
    },
    {
        "QuestionText": "<b>1. Which Evening & Weekend MBA (EWMBA) cohort are you in?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "Evening Blue (Monday/Wednesday)" },
            "2": { "Display": "Evening Gold (Tuesday/Thursday)" },
            "3": { "Display": "Weekend (Saturday)" },
            "4": { "Display": "Lux / Nexus (Flex)" },
            "5": { "Display": "Other / Dual Degree" }
        },
        "ChoiceOrder": ["1", "2", "3", "4", "5"],
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None"
            }
        }
    },
    {
        "QuestionText": "<b>2. What is your primary mode of transportation when commuting to Haas?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "Drive alone (personal vehicle)" },
            "2": { "Display": "Carpool with classmate(s)" },
            "3": { "Display": "BART" },
            "4": { "Display": "AC Transit (bus)" },
            "5": { "Display": "Rideshare (Uber/Lyft)" },
            "6": { "Display": "CalTrain / Capitol Corridor" },
            "7": { "Display": "Walk / Bike / Scooter" },
            "8": { "Display": "Other" }
        },
        "ChoiceOrder": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None"
            }
        }
    },
    {
        "QuestionText": "<b>3. What is your departure ZIP code or city when commuting to campus?</b>",
        "QuestionType": "TE",
        "Selector": "SL"
    },
    {
        "QuestionText": "<b>4. On average, how long is your one-way commute to Haas?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "Under 30 minutes" },
            "2": { "Display": "30 - 45 minutes" },
            "3": { "Display": "45 - 60 minutes" },
            "4": { "Display": "60 - 90 minutes" },
            "5": { "Display": "Over 90 minutes" }
        },
        "ChoiceOrder": ["1", "2", "3", "4", "5"]
    },
    {
        "QuestionText": "<b>5. How would you rate your satisfaction with the following aspects of commuting to Haas?</b>",
        "QuestionType": "Matrix",
        "Selector": "Likert",
        "SubSelector": "SingleAnswer",
        "Choices": {
            "1": { "Display": "Highly Dissatisfied" },
            "2": { "Display": "Somewhat Dissatisfied" },
            "3": { "Display": "Neutral" },
            "4": { "Display": "Somewhat Satisfied" },
            "5": { "Display": "Highly Satisfied" }
        },
        "Answers": {
            "1": { "Display": "Parking availability near campus" },
            "2": { "Display": "Parking cost" },
            "3": { "Display": "Safety of commute / walk to campus at night" },
            "4": { "Display": "Public transit reliability to campus" },
            "5": { "Display": "Haas communication/support regarding commute logistics" }
        },
        "ChoiceOrder": ["1", "2", "3", "4", "5"],
        "AnswerOrder": ["1", "2", "3", "4", "5"]
    },
    {
        "QuestionText": "<b>6. How well do the new commuting and parking logistics align with the premium experience expected of a top-tier MBA program for working professionals?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "1 - Not at all aligned" },
            "2": { "Display": "2 - Slightly aligned" },
            "3": { "Display": "3 - Moderately aligned" },
            "4": { "Display": "4 - Well aligned" },
            "5": { "Display": "5 - Perfectly aligned" }
        },
        "ChoiceOrder": ["1", "2", "3", "4", "5"]
    },
    {
        "QuestionText": "<b>7. How often have parking or transit delays directly disrupted your academic schedule (e.g., arriving late to class, missing a lecture, or missing scheduled group meetings)?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "Never" },
            "2": { "Display": "Rarely (1-2 times per semester)" },
            "3": { "Display": "Occasionally (3-5 times per semester)" },
            "4": { "Display": "Frequently (6+ times per semester)" }
        },
        "ChoiceOrder": ["1", "2", "3", "4"]
    },
    {
        "QuestionText": "<b>8. If a prospective applicant with a similar professional and geographical profile asked for your honest advice about joining Haas, how would you suggest they view the new commuting and parking situation?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "It is a non-issue (not a factor in the decision)." },
            "2": { "Display": "It is a minor factor (manageable annoyance, but should not affect enrollment)." },
            "3": { "Display": "It is a significant factor (should be weighed against competing programs like Wharton SF or Stanford)." },
            "4": { "Display": "It is a critical factor (should actively discourage enrolling unless they live near campus)." }
        },
        "ChoiceOrder": ["1", "2", "3", "4"]
    },
    {
        "QuestionText": "<b>9. How frequently do you use UC Berkeley transit services (e.g., the Class Pass for AC Transit buses, or Bear Transit campus shuttles) to commute to campus?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "Never" },
            "2": { "Display": "Rarely (1-2 times per semester)" },
            "3": { "Display": "Occasionally (1-2 times per month)" },
            "4": { "Display": "Frequently (Weekly or daily)" }
        },
        "ChoiceOrder": ["1", "2", "3", "4"]
    },
    {
        "QuestionText": "<b>10. The mandatory campus transit fee (UC Berkeley Class Pass) is automatically charged to all students. If given the option, would you choose to opt-out of this fee to reduce your semester tuition/fees?</b>",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Choices": {
            "1": { "Display": "Yes, I would choose to opt out of the fee." },
            "2": { "Display": "No, I would choose to remain opted in." }
        },
        "ChoiceOrder": ["1", "2"]
    },
    {
        "QuestionText": "<b>11. Do you have any additional comments, feedback, or suggestions regarding commuting and parking for EWMBA students?</b>",
        "QuestionType": "TE",
        "Selector": "ESTB"
    }
]

# 3. Add questions programmatically
for i, q in enumerate(questions):
    print(f"Adding question {i+1} of {len(questions)}...")
    url = f"{BASE_URL}/survey-definitions/{survey_id}/questions?blockId={block_id}"
    
    if i == 0:
        q["DataExportTag"] = "Intro"
    else:
        q["DataExportTag"] = f"Q{i}"
        
    status, resp = make_request(url, "POST", q)
    if status == 200:
         print(f"Added Q{i+1} (tag: {q['DataExportTag']}): {resp['result']['QuestionID']}")
    else:
         print(f"Failed to add Q{i+1}: {resp}")
         exit(1)
    time.sleep(0.5)

print("\nAll questions added successfully!")
print(f"Survey URL to access in Qualtrics: https://{DATA_CENTER}.qualtrics.com/survey-builder/{survey_id}/edit")
