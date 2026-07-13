# UC Berkeley Haas EWMBA Commuter Survey Design

*Prepared for Dean Review / Advocacy Proposal*

This document outlines the final, unbiased survey design to advocate for better commute options for the Evening & Weekend MBA (EWMBA) class at UC Berkeley Haas, sponsored by the Evening & Weekend MBA Association (EWMBAA) officers.

---

## 1. Survey Objectives & Methodology
The objective of this survey is to collect rigorous, objective, and actionable data regarding the EWMBA commuter experience. To ensure the results carry administrative weight and cannot be dismissed as biased or leading:
1.  **Neutral Language:** Questions avoid assuming the commute is a problem, instead measuring satisfaction, impact, and willingness-to-pay (WTP) symmetrically.
2.  **De-bundled Solutions:** Parking and public transit options are split to avoid "double-barreled" errors.
3.  **Behavior Segmented Data:** Policy preferences are measured independently from behavioral usage (e.g., separating how often students use the transit pass from whether they want to opt out).

---

## 2. Revisions to Remove Bias

Here are the specific changes made to the draft questions to optimize them for administrative and Dean-level review:

### Question 7 (Draft Question 2): Premium Experience Alignment
*   **Draft Phrasing:** *"To what extent do you agree with this statement: 'The current commuting logistics align with the premium experience expected of a top-tier MBA program for working professionals'?"*
*   **Revised Phrasing:** **"How well do the new commuting and parking logistics align with the premium experience expected of a top-tier MBA program for working professionals?"**
*   **Response Scale:** 1 to 5 (*Not at all aligned* to *Perfectly aligned*)
*   **Rationale:** Changing from statement-agreement to direct evaluation eliminates **acquiescence bias** (the tendency of respondents to agree with assertions), producing more objective sentiment data.

### Question 9 (Draft Question 1): Advice to Prospective Students
*   **Draft Phrasing:** *"...how heavily would you advise them to factor in the current commuting/parking situation?"*
*   **Revised Phrasing:** **"...how would you suggest they view the new commuting and parking situation?"**
*   **Response Options:**
    *   *It is a non-issue (not a factor in the decision).*
    *   *It is a minor factor (manageable annoyance, but should not affect enrollment).*
    *   *It is a significant factor (should be weighed against competing programs like Wharton SF or Stanford).*
    *   *It is a critical factor (should actively discourage enrolling unless they live near campus).*
*   **Rationale:** Neutralized the prompt to avoid leading the respondent to think they *must* recommend factoring it in, and balanced the options to represent a clean gradient of severity.

### Questions 12 & 13 (Draft Question 3): Willingness to Pay (WTP)
*   **Draft Phrasing:** *"If Haas offered a guaranteed, hassle-free parking or premium transit solution..."*
*   **Revised Action:** **Split into two separate questions (Parking vs. Transit).**
*   **Revised Choices:** Changed "$0 (The school should absorb this cost)" to **"$0 (I would not pay extra / it should be included in tuition)"**.
*   **Rationale:** Bundling parking and transit is "double-barreled"—drivers and transit riders value different solutions. Splitting them gives the administration precise data on where to direct budget (e.g., parking contracts vs. shuttle services). Removing policy justifications from the "$0" option ensures students respond based on economic willingness rather than policy protests.

### Questions 10 & 11 (Draft Question 4): AC Transit Fee Opt-Out
*   **Draft Phrasing:** *"Yes, I do not use it and want to opt out / No, I use it or want to keep supporting..."*
*   **Revised Action:** **Separated into a usage frequency question (Q10) followed by a policy preference question (Q11).**
*   **Revised Choices for Q11:**
    *   *Yes, I would choose to opt out of the fee.*
    *   *No, I would choose to remain opted in.*
*   **Rationale:** Respondents often want to support public transit even if they don't personally use it, or they might use it very rarely but still prefer to save tuition. Separating usage frequency from the opt-out preference lets you present the Dean with clear statistics (e.g., *"X% of students never use the pass, and Y% of those students would choose to opt out if given the choice"*).

---

## 3. Active Survey Link

The survey is active on your UC Berkeley Qualtrics account:
👉 **[Haas EWMBA Commuter Survey on Qualtrics](https://berkeley.qualtrics.com/survey-builder/SV_74HH3uxPuJREtIq/edit)**

### Current Survey Flow & Questions:
1.  **Intro Block (Text / Graphic):** *"Haas EWMBA Commuter Survey: Help us advocate for better commuting and parking options at Haas. This 3-minute survey is conducted by your EWMBA Association (EWMBAA) officers. Your responses are completely anonymous, confidential, and will be shared directly with Haas leadership."*
2.  **Q1 (MC - MANDATORY):** Which Evening & Weekend MBA (EWMBA) cohort are you in?
    *   *Choices:* Evening Blue (Monday/Wednesday), Evening Gold (Tuesday/Thursday), Weekend (Saturday), **Lux / Nexus (Flex)**, Other / Dual Degree.
3.  **Q2 (MC - MANDATORY):** What is your primary mode of transportation when commuting to Haas?
4.  **Q3 (TE):** What is your departure ZIP code or city when commuting to campus?
5.  **Q4 (MC):** On average, how long is your one-way commute to Haas?
6.  **Q5 (Matrix):** Satisfaction with parking availability, cost, safety, public transit, and Haas support.
7.  **Q6 (MC):** **How well do the new commuting and parking logistics align with the premium experience expected of a top-tier MBA program for working professionals?**
8.  **Q7 (MC):** How often have commuting or parking difficulties caused you to be late for class, miss class, or miss networking/group work?
9.  **Q8 (MC):** **If a prospective applicant with a similar professional and geographical profile asked for your honest advice about joining Haas, how would you suggest they view the new commuting and parking situation?**
10. **Q9 (MC):** How frequently do you use the mandatory AC Transit Class Pass (bus pass) to commute to campus?
11. **Q10 (MC):** Would you choose to opt-out of the transit fee if given the option?
12. **Q11 (MC):** For a hypothetical program providing guaranteed, hassle-free parking exclusively for professional students on class days, what is the maximum amount you would be willing to pay out-of-pocket PER SEMESTER?
13. **Q12 (MC):** For a hypothetical program providing a premium transit solution (e.g., dedicated shuttles, subsidized rideshare partnerships, or express transit credits) exclusively for professional students on class days, what is the maximum amount you would be willing to pay out-of-pocket PER SEMESTER?
14. **Q13 (TE):** Additional comments, feedback, or suggestions.

---

## 4. Post-Import Settings in Qualtrics (Actions Required)

Please apply these final two settings in your Qualtrics editor to finish the survey setup:
1.  **Add Display Logic for Willingness-to-Pay (WTP):**
    *   Click on **Q11 (Parking WTP)** $\rightarrow$ scroll down the left sidebar $\rightarrow$ click **Add Display Logic** $\rightarrow$ set it to show only if **Q2 (Transit Mode)** is *Drive alone* or *Carpool*.
    *   Click on **Q12 (Transit WTP)** $\rightarrow$ click **Add Display Logic** $\rightarrow$ set it to show only if **Q2** is *BART*, *AC Transit*, or *CalTrain / Corridor*.
2.  **Add Page Breaks:**
    *   Hover between questions and click **Add Page Break** after **Q4** (demographic profile page), after **Q7** (experience page), and after **Q10** (AC Transit pass page).
