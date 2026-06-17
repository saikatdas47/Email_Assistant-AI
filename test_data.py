TEST_SCENARIOS = [
    {
        "id": 1,
        "intent": "Follow up after a product demo to close the deal.",
        "facts": ["Client loved the new dashboard feature.", "Awaiting budget approval from their finance team.", "We should send them the case study."],
        "tone": "formal",
        "reference": "Subject: Follow-Up on Product Demo\n\nDear Team,\n\nI hope you are having a productive week. Following our recent product demonstration, I wanted to follow up and gauge your thoughts. We were thrilled to see how much your team loved the new dashboard feature. \n\nI understand that you are currently awaiting budget approval from your finance department. In the meantime, I am sending over our detailed case study, which highlights the ROI achieved by similar companies.\n\nPlease let me know if you have any questions or if we can schedule another session to address any concerns.\n\nBest regards,\n[Your Name]"
    },
    {
        "id": 2,
        "intent": "Request specific technical details for a proposal.",
        "facts": ["Project name: Project X.", "Deadline is July 15.", "Need the technology stack used in their solution."],
        "tone": "urgent",
        "reference": "Subject: URGENT: Request for Proposal Details - Project X\n\nHi Team,\n\nI am reaching out regarding the proposal for Project X. Given the strict July 15 deadline, we need to finalize our technical alignment immediately.\n\nCould you please send over the complete technology stack used in your proposed solution as soon as possible? \n\nWe appreciate your cooperation and look forward to receiving this information today.\n\nRegards,\n[Your Name]"
    },
    {
        "id": 3,
        "intent": "Apologize for a delayed response to a client.",
        "facts": ["There was a server outage that caused the delay.", "The issue is now fully resolved.", "We are offering a 10% discount as a goodwill gesture."],
        "tone": "empathetic",
        "reference": "Subject: Sincere Apologies for the Delay\n\nDear Client,\n\nI am writing to sincerely apologize for the delay in our response. We recently experienced an unexpected server outage, which unfortunately impacted our communication channels and response times. \n\nPlease be assured that the issue has now been fully resolved, and our systems are running smoothly. As a small token of our sincere apology for the inconvenience, we would like to offer you a 10% discount on your next invoice.\n\nWe truly value your partnership and are taking steps to prevent this from happening again.\n\nWarm regards,\n[Your Name]"
    },
    {
        "id": 4,
        "intent": "Casual invite for team lunch.",
        "facts": ["Lunch is on Friday at 1 PM.", "Venue is the Italian place downtown.", "Please RSVP by Wednesday."],
        "tone": "casual",
        "reference": "Subject: Team Lunch this Friday!\n\nHey everyone,\n\nLet's take a break this Friday and grab some lunch together! We're heading to that awesome Italian place downtown at 1 PM. \n\nCould you please let me know if you're coming by Wednesday so I can book the right number of seats? \n\nCheers,\n[Your Name]"
    },
    {
        "id": 5,
        "intent": "Formal complaint about a damaged shipment.",
        "facts": ["Order number is #1234.", "The goods arrived damaged.", "We need a replacement shipped immediately."],
        "tone": "formal",
        "reference": "Subject: Formal Complaint - Damaged Shipment (Order #1234)\n\nDear Supplier,\n\nI am writing to formally lodge a complaint regarding our recent shipment, reference Order #1234. Upon inspection, it was discovered that the goods arrived in a severely damaged condition. \n\nWe request that you arrange for a replacement to be shipped to us immediately. Please confirm the shipping timeline at your earliest convenience.\n\nWe trust you will take this matter seriously to maintain our professional relationship.\n\nYours faithfully,\n[Your Name]"
    },
    {
        "id": 6,
        "intent": "Thank a partner for successful collaboration.",
        "facts": ["Q3 revenue increased by 20%.", "Looking forward to Q4 planning.", "Suggest a virtual meet to discuss next steps."],
        "tone": "empathetic",
        "reference": "Subject: A Heartfelt Thank You for Q3 Success\n\nDear Partner,\n\nI wanted to take a moment to express my sincere gratitude for your hard work and collaboration this quarter. Thanks to our joint efforts, we have successfully increased our Q3 revenue by an outstanding 20%.\n\nThis achievement fills us with optimism for Q4. I would like to suggest scheduling a virtual meet to discuss our strategic planning and next steps for the upcoming quarter.\n\nI look forward to continuing our journey together.\n\nWith appreciation,\n[Your Name]"
    },
    {
        "id": 7,
        "intent": "Notify about a critical security patch.",
        "facts": ["Critical vulnerability detected.", "Patch must be applied by Friday.", "Attached list of affected servers."],
        "tone": "urgent",
        "reference": "Subject: CRITICAL: Security Patch Required by Friday\n\nAll Staff,\n\nThis is a critical security alert. A vulnerability has been detected in our current system that requires immediate attention.\n\nAll teams must apply the recommended patch no later than this Friday. Please find the attached list of affected servers for your reference. \n\nDelays beyond this timeline will compromise our network integrity.\n\nAct now.\n\nIT Administration"
    },
    {
        "id": 8,
        "intent": "Negotiate lower pricing with a vendor.",
        "facts": ["Current pricing is too high.", "Competitor offers 15% less.", "Propose a new bulk rate."],
        "tone": "formal",
        "reference": "Subject: Proposal for Revised Pricing Structure\n\nDear Vendor,\n\nWe have reviewed your latest quotation and find that the current pricing structure is significantly above our projected budget. As we value our ongoing relationship, we would like to discuss a mutually beneficial adjustment.\n\nOur market research indicates that a competitor is offering a similar service at roughly 15% lower. To sustain our collaboration, we would like to propose a new, competitive bulk rate that reflects current market standards.\n\nWe are open to negotiation and hope to reach an agreement soon.\n\nSincerely,\n[Your Name]"
    },
    {
        "id": 9,
        "intent": "Ask for leave approval from manager.",
        "facts": ["Requesting 2 weeks off in August.", "Project handover will be given to Jane.", "Will be available via email for emergencies."],
        "tone": "formal",
        "reference": "Subject: Request for Leave Approval - August\n\nDear Manager,\n\nI am writing to formally request a leave of absence for 2 weeks during the month of August. \n\nTo ensure continuity, I will prepare a comprehensive handover of my current projects to Jane. Should any critical emergencies arise during my absence, I will be available via email.\n\nPlease let me know if you require any further information.\n\nYours sincerely,\n[Your Name]"
    },
    {
        "id": 10,
        "intent": "Share meeting minutes with the team.",
        "facts": ["The team decided to rebrand with a new logo.", "The marketing budget has been increased.", "Next meeting is scheduled for the 10th."],
        "tone": "casual",
        "reference": "Subject: Meeting Minutes - Rebranding & Budget\n\nHi Team,\n\nThanks for the great discussion today! Here’s a quick recap:\n- We decided to move forward with the new logo for our rebranding campaign.\n- The marketing budget has officially been increased, so we have more room to play with.\n\nOur next sync is scheduled for the 10th of next month. See you all then!\n\nCheers,\n[Your Name]"
    }
]