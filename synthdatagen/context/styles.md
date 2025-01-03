# Oncology Letter Styles

This section contains descriptions of letter styles. For the purposes of synthetic letter generation, these styles can (and should) be customised to represent local and varied oncology letters.
* Language styles describes possible ways of expressing information that might be adopted by a letter writer, including verbosity, complexity, and formality of language.
* Formatting / Data Quality describes objective characteristics of real-world letters
* Structural styles contain examples of different type of letter structure. These are followed by an entirely synthetic (but realistic) example of the given style.

## Language Styles
* Concise and factual structured sections, that often precede narrative text styles. Example:
```
Diagnosis:\t\tEndometrial cancer\n\nManagement:\t\t22 Mar 2024 Total abdominal hysterectomy and bilateral salpingo-oophorectomy\n\nHistology:\tGrade 2 endometrioid adenocarcinoma, stage pT2, N0M0 with lymphovascular space invasion present\n\nCurrent Situation:\tSeen prior to cycle 4 Carboplatin/Paclitaxel\n\nI
```
* Verbose narrative using professional language with detailed clinical description. Example:
```
Her symptoms began approximately four months ago with a persistent cough, gradually worsening breathlessness and right-sided chest pain. She has noted significant weight loss of about 8kg over this period and increasing fatigue. Currently her performance status is 1 and she requires a walking frame due to bone pain affecting her spine and left hip.? She describes ongoing chest pain requiring regular paracetamol and codeine.??\n?\nIn her past medical history, she has significant Type 1 diabetes with peripheral neuropathy
```
* Brief, business-like narrative, resulting in relatively short length compared to typical oncology letters. Example:
```
[redacted name] attended today's Breast Oncology Clinic at Guy's Hospital.? She has had a left sided chemo port insertion done yesterday and has no acute issues at the moment.? Her bloods show that her parameters are acceptable for chemotherapy and I have prescribed the same on our system, which will be done on the Chemo Day Unit.? I am happy to proceed with cycle one of chemotherapy and see her in clinic in three weeks' time.
```
* Verbose narrative sections with informal, empathetic, descriptive, and patient-centric tone ("very pleased", "really doing her very best"). Example:
```
I was very pleased to review [redacted name] who attended the nurse and pharmacy lead clinic today. She is managing the treatment relatively well. She is finding it challenging but is making excellent efforts to maintain her fitness during chemotherapy. She continues with gentle walking daily, though her work as a teacher has become more demanding. She reports feeling somewhat anxious and overwhelmed at present, so at her request I have made a referral to our psychology support service.
```

## Formatting / Data Quality
* Multiple paragraphs separated by double newlines (\n?\n)
* Question marks (?) as apparent formatting artifacts
* Contains multiple tab characters (\t) and newline symbols (\n)
* Data quality issues include inconsistent spacing, unexpected characters

## Structural Styles

### Standard Narrative Letter
* Opens with diagnosis heading marked "Diagnosis:", no use of additional headers
* Follows with timeline of events for primary cancer
* Transitions to narrative format after this initial section
* Narrative format signposts subblocks, such as "In her past medical history", and "Her current medications include".
* Dates are used to reinforce particular historical narrative items
```
Diagnosis:\tT4 N2 M1c non-small cell lung cancer (adenocarcinoma) with widespread bone metastases, adrenal metastases and contralateral lung nodules.?\n\tCT chest 15 March 2024 - 6.8cm right upper lobe mass with mediastinal and hilar lymphadenopathy.?\n\tPET-CT 18 March 2024 - FDG-avid right upper lobe primary with widespread skeletal metastases and bilateral adrenal metastases.?\n\tMRI brain 20 March 2024 - No evidence of intracranial metastases.??\n?\n[redacted name] is a 52 year old lady who has unfortunately recently been diagnosed with adenocarcinoma of the lung with widespread metastatic disease affecting multiple bones and both adrenal glands. Her symptoms began approximately four months ago with a persistent cough, gradually worsening breathlessness and right-sided chest pain. She has noted significant weight loss of about 8kg over this period and increasing fatigue. Currently her performance status is 1 and she requires a walking frame due to bone pain affecting her spine and left hip.? She describes ongoing chest pain requiring regular paracetamol and codeine.??\n?\nIn her past medical history, she has significant Type 1 diabetes with peripheral neuropathy, chronic migraine, fibromyalgia, depression, and hypothyroidism. She also has a long-standing history of anxiety for which she takes regular medication.?\n?\nShe lives with her husband who provides good support with daily activities.? She is an ex-smoker having quit 5 years ago with a 30 pack-year history. She drinks minimal alcohol. She has three children aged 28, 25 and 23, and her eldest daughter attended today's appointment.?\n?\nHer current medications include insulin (Lantus and NovoRapid), levothyroxine, amitriptyline, pregabalin, sertraline, metoclopramide, and regular paracetamol and codeine for pain.?She mentioned recently stopping her amitriptyline due to increased drowsiness.?\n?\nImaging shows a large right upper lobe mass on CT chest done on 15/3/24 with associated mediastinal lymphadenopathy.? PET-CT on 18 March 2024 confirmed widespread skeletal metastases and bilateral adrenal involvement.? An MRI brain has fortunately shown no evidence of brain metastases.?\n?\nOn clinical examination, there is reduced air entry in the right upper zone with some surrounding percussion dullness. There is tenderness over the left hip and thoracic spine. No neurological deficits are identified.??\n?\nI have discussed her case with [redacted name] and [redacted name] was also reviewed by him during today's clinic. [redacted name] outlined the role of systemic anti-cancer therapy, potential palliative radiotherapy to symptomatic bone sites, and the importance of molecular testing to guide treatment selection.? We have discussed chemotherapy/immunotherapy combinations, focusing on the carboplatin/pemetrexed/pembrolizumab regimen - including procedure and common side effects.? We have arranged urgent molecular testing (EGFR, ALK, ROS1, PDL1) and will be referring her case for discussion at next week's Lung MDT.?\n\nI have requested molecular testing, booked a bone density scan, referred to acute oncology for consideration of urgent zoledronic acid, and completed the MDT referral.? I have provided written information about systemic therapy options and we will review her in clinic with molecular results and MDT outcome in 10 days? time. Please do not hesitate to contact us if any further information is required.?
```

### Short Structured Letter
* Structured throughout with clear subheadings (Diagnosis, Management, Histology, Current situation)
* Concise and focused only on essential information for each subheading
* Information organized in key-value pairs under headings
```
Diagnosis:?\t\tMetastatic breast carcinoma?\n?\nManagement:\t\t15.09.23 Wide local excision and axillary clearance?\n?\nHistology:\t\tGrade 3 invasive ductal carcinoma stage \npT2 N2 (6/18) M1\nER/PR negative, HER2 positive?\n\nCurrent situation:\tSeen pre-cycle one TCHP.\n?\n[redacted name] attended today's Breast Oncology Clinic at Guy's Hospital.? She has had a left sided chemo port insertion done yesterday and has no acute issues at the moment.? Her bloods show that her parameters are acceptable for chemotherapy and I have prescribed the same on our system, which will be done on the Chemo Day Unit.? I am happy to proceed with cycle one of chemotherapy and see her in clinic in three weeks' time. Please do not hesitate to contact us if any further information is desired.
```

## Standard Semi-Structured Letter
* Opens with structured key data in clear sections (Diagnosis, Management, Histology, Current Situation)
* Transitions to narrative format for current assessment
* No subheadings in narrative portion
```
Diagnosis:\t\tEndometrial cancer\n\nManagement:\t\t22 Mar 2024 Total abdominal hysterectomy and bilateral salpingo-oophorectomy\n\nHistology:\tGrade 2 endometrioid adenocarcinoma, stage pT2, N0M0 with lymphovascular space invasion present\n\nCurrent Situation:\tSeen prior to cycle 4 Carboplatin/Paclitaxel\n\nI was very pleased to review [redacted name] who attended the nurse and pharmacy lead clinic today. She is managing the treatment relatively well. She is finding it challenging but is making excellent efforts to maintain her fitness during chemotherapy. She continues with gentle walking daily, though her work as a teacher has become more demanding. She reports feeling somewhat anxious and overwhelmed at present, so at her request I have made a referral to our psychology support service. She has grade 1 peripheral neuropathy affecting her fingertips only, which she manages with regular moisturizing. She has no neuropathy in her feet. She describes some alterations in taste sensation due to the chemotherapy. Her previous pelvic discomfort has improved with regular paracetamol and as recommended by Dr [redacted name]. She has developed dry mouth and eyes, and I have prescribed artificial tear drops today. \n\nThe plan is to proceed with cycle 4 and we will see her again in this clinic in three weeks? time
```

### Highly Structured Summary
* Highly structured with clear delineation between sections
* Nested narrative consultation summary appearing in Consultation section
* Structured section content is often bullet-pointed or numbered (for example, diagnoses, treatment history)
* Specific structure as follows:
1. Diagnosis
   - Numbered list of conditions
   - Date of diagnosis
   - Treatment aim
2. Summary of completed treatment and relevant dates
   - Surgery
   - Radiotherapy
   - Chemotherapy
   - Clinical studies
3. Current disease status
4. Current issues
5. Summary of consultation
   [Narrative section]
6. Further investigations
7. Medication prescribed
8. Follow up
   - Next oncology follow up
   - Next surgical follow up
9. Required GP actions
* Highly detailed multi-step action plan
```
Diagnosis\n\t1. Squamous cell carcinoma (SCC) T2N1 of left floor of mouth\n\n2. Basal cell carcinoma of left temple\n\n      3   Controlled rheumatoid arthritis since 2015\n\n\tDate of diagnosis\n\tJanuary 2024\n\n\tTreatment aim\n\tCurative      \n\n\tSummary of completed treatment and relevant dates\n\n\tSurgery\n\t12 Jan 2024 Oral cavity biopsy and temple lesion biopsy performed by Mr [redacted name]\n\n\tRadiotherapy\n\t15 Feb 2024 ? 22 Mar 2024 to complete\n\n1.  Radical intensity modulated radiotherapy (IMRT) 65Gy in 30 fractions to oral cavity and left neck level IB-II\n\n2. Superficial radiotherapy to left temple lesion\n\n\tChemotherapy\n\tNot indicated\n\n\tClinical studies\n\tNone\n\n\tCurrent disease status\n\tNo evidence of disease\n\n\tCurrent issues\n\tDry mouth\n\n\tSummary of consultation \n\tThis 82 year old gentleman attended clinic today accompanied by his daughter.  \n\nIt has been four weeks since he completed a course of radiotherapy to the floor of mouth and also to the left temple region. I am pleased to report that he managed the treatment remarkably well. He developed the expected mucositis with pain on swallowing and speech, along with a localized skin reaction in the temple region. These side effects are now showing good improvement.\n\n On review today, his speech is much clearer although he reports ongoing dry mouth. The temple area is healing well. His swallowing has improved significantly though he still requires frequent sips of water with meals. His main ongoing challenge is dry mouth, though he is managing a near-normal diet.\n\n On examination, there was no palpable neck disease and the oral cavity showed expected post-radiation changes but no concerning features. His speech was clear. I will perform detailed oral cavity examination at his next appointment.\n\nWe will see him in six weeks time for thorough oral cavity assessment. I have explained that we will consider whether imaging is indicated at that point, but currently there are no immediate concerns requiring investigation.\n\n\tFurther investigations\n\tNone\n\n\tMedication prescribed\n\tNone\n\n\tFollow up\n\tNext oncology follow up will be in six weeks\nNext surgical follow up will be with Mr. [redacted name]. ? Could Mr. [redacted name] organise follow up please.\n\n\tRequired GP actions \n\tPlease monitor inflammatory markers, renal function and any age-appropriate checks - including dental review as patient has had radiation to oral cavity \n\n\tSummary of information given to the patient about their cancer and future progress \n\t[redacted name] understands that we have treated with curative intent and that he appears to have responded well to treatment. We will assess this more thoroughly at his three month post-treatment appointment.
```

### Block-Label Format
* Opens with "Diagnosis:" header followed by diagnosis statement
* Uses clear block headers ("Previous medical history:", "Current medications:")
* Each block contains list of concise information
* Follows with "Current Situation:" statement
* Ends with longer narrative style assessment without headers
```
Diagnosis:\n\nMetastatic colorectal adenocarcinoma\n\nSurgery 20 March 2024 ? Dr [redacted name] ? Large sigmoid mass with peritoneal deposits. Palliative bypass performed. Biopsy confirmed moderately differentiated adenocarcinoma with signet ring features.\n\nPrevious medical history:\nChronic obstructive pulmonary disease, Atrial fibrillation, Essential hypertension\n\nCurrent medications:\nApixaban and Salbutamol inhaler\n\nAllergies:\n\nPenicillin - rash\n\nCurrent situation:\nCompleted first cycle of FOLFOX chemotherapy\n\nCT scan 15 April ? stable appearances of peritoneal disease\n\nOverall stable disease picture\n\nCEA trending down to 45\n\nPre cycle 2 FOLFOX\nI reviewed [redacted name] today who attended for assessment before cycle 2 FOLFOX. The first cycle was well tolerated with only grade 1 nausea and mild fatigue. Performance status remains 1. Appetite is improving and weight has stabilized. Examination shows no new concerns and bloods are satisfactory for proceeding with treatment. The plan is to continue with cycle 2 today and follow up before cycle 3 in the Thursday clinic. All questions were addressed and [redacted name] understands to contact us if any problems develop.
```

### Fully Narrative Letter
* Direct opening acknowledging referral or consultation (for example "Many thanks for referring" or "I was pleased to see...")
* Single continuous narrative without headers
* Detailed discussion and consideration of clinical topics, including outlining thought processes
```
Many thanks for referring [redacted name] who I met with his daughter.\n\nHe is a 58 year old gentleman who has undergone anterior resection for sigmoid cancer with 3/12 lymph nodes positive and is currently receiving adjuvant chemotherapy. CT scans have shown a 2cm right upper lobe pulmonary nodule that has demonstrated interval growth on sequential CTs. He has significant asbestos exposure from his work as a plumber but is otherwise extremely fit and well.\n\nI have explained to [redacted name] that this nodule is enlarging and we are highly suspicious that it could represent some form of malignancy. This may be a primary lung cancer given his asbestos exposure but it could also represent a metastatic deposit from his sigmoid cancer. It could also represent something entirely different altogether, either benign or malignant. I think that it is very reasonable to excise this in the form of a VATS wedge excision with frozen section analysis. I have explained to him that we would perform our best estimate at this time but if there was evidence that it was likely to be a lung cancer we would proceed to a lobectomy. [redacted name] would fully tolerate this as he is an extremely fit man and would still be left with 70% of his lung. The risk of this procedure in this case is fairly minimal with risks of infection, bleeding and a small risk to life of about 1% or so. A full description of the risks and benefits is detailed below and he will have an opportunity to ask further questions when he arrives at the hospital. He wishes to have this done after completing his current chemotherapy cycle. I will give him an appointment and shall keep you informed.\n\n(pain, drainage, prolonged drainage, risk to intrathoracic structures,?further lung resection, enlargement of incision, rib fracture, potential of diagnosis of unexpected pathology both benign and malignant, PE, cardiac event, stroke, respiratory complications, intubation and intensive care admission, other medical or surgical complications and the?risk to life, which is low but not zero.?The goal of the surgical team will be to diagnose fully and treat the underlying condition and to exclude potentially serious conditions. Occasionally findings at surgery may alter the nature of the operation, even taking into account pre and intra-operative tests).
```
