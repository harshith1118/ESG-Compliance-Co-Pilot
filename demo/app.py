import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
import yaml
from io import BytesIO
import json

# Set page config
st.set_page_config(
    page_title="ESG Compliance Co-Pilot",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0066cc;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .agent-card {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 4px solid #0066cc;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .warning-message {
        background-color: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'compliance_data' not in st.session_state:
    st.session_state.compliance_data = {}
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False

def main():
    st.markdown('<h1 class="main-header">🌱 ESG Compliance Co-Pilot</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("../assets/cover_art.svg", use_column_width=True)
        st.header("Project Information")
        st.write("**Problem**: Manual ESG reporting takes 200+ hours/month")
        st.write("**Solution**: AI-powered automation with 40x speed improvement")
        st.write("**Technology**: IBM watsonx Orchestrate + Streamlit")
        
        # Step navigation
        st.header("Process Steps")
        steps = [
            "Upload Data Sources",
            "Regulation Mapping",
            "Compliance Analysis",
            "Generate Report"
        ]
        
        for i, step in enumerate(steps):
            if i <= st.session_state.current_step:
                st.success(f"✅ {step}")
            else:
                st.info(f"ℹ️ {step}")
        
        st.header("Performance Metrics")
        st.metric("Time Reduction", "40x", "200 hours → 5 minutes")
        st.metric("Accuracy", "95%", "53% → 95%")
        st.metric("Risk Mitigation", "$1.8M", "Potential fines avoided")

    # Main content
    if st.session_state.current_step == 0:
        upload_data_sources()
    elif st.session_state.current_step == 1:
        regulation_mapping()
    elif st.session_state.current_step == 2:
        compliance_analysis()
    elif st.session_state.current_step == 3:
        generate_report()

def upload_data_sources():
    st.header("Step 1: Upload Data Sources")
    
    st.write("""
    Upload ESG data from your enterprise systems. Our Data Hunter Agent will automatically:
    - Extract relevant ESG metrics
    - Normalize data formats
    - Identify data gaps
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data Sources")
        erp_file = st.file_uploader("ERP Data (CSV/Excel)", type=['csv', 'xlsx'])
        hris_file = st.file_uploader("HRIS Data (CSV/Excel)", type=['csv', 'xlsx'])
        
    with col2:
        st.subheader("Financial Data")
        finance_file = st.file_uploader("Finance Data (CSV/Excel)", type=['csv', 'xlsx'])
        other_files = st.file_uploader("Other Sources (multiple)", type=['csv', 'xlsx'], accept_multiple_files=True)
    
    if st.button("Process Data Sources", key="process_sources"):
        if not any([erp_file, hris_file, finance_file, other_files]):
            st.warning("Please upload at least one data file")
            return
            
        # Simulate data processing
        with st.spinner("Processing data sources with Data Hunter Agent..."):
            time.sleep(2)
            
            # Mock data collection
            st.session_state.compliance_data['data_collection'] = {
                'erp_data': 1247,
                'hris_data': 856,
                'finance_data': 932,
                'other_data': 543,
                'total_records': 3578
            }
            
            st.session_state.compliance_data['data_gaps'] = [
                {'field': 'Scope 3 Emissions', 'source': 'Supply Chain', 'severity': 'High'},
                {'field': 'Water Usage', 'source': 'Facilities', 'severity': 'Medium'},
                {'field': 'Diversity Metrics', 'source': 'HR', 'severity': 'Low'}
            ]
        
        st.success("✅ Data sources processed successfully!")
        st.session_state.current_step = 1
        
        # Display mock results
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Collected Data Summary")
            data_summary = st.session_state.compliance_data['data_collection']
            st.write(f"ERP Records: {data_summary['erp_data']}")
            st.write(f"HRIS Records: {data_summary['hris_data']}")
            st.write(f"Finance Records: {data_summary['finance_data']}")
            st.write(f"Other Records: {data_summary['other_data']}")
            st.write(f"**Total Records: {data_summary['total_records']}**")
        
        with col2:
            st.subheader("Data Gaps Identified")
            for gap in st.session_state.compliance_data['data_gaps']:
                st.warning(f"⚠️ {gap['field']} ({gap['severity']} priority) from {gap['source']}")

def regulation_mapping():
    st.header("Step 2: Regulation Mapping")
    
    st.write("""
    The Regulation Decoder Agent maps your collected data to specific compliance requirements:
    - CSRD (Corporate Sustainability Reporting Directive)
    - GRI (Global Reporting Initiative)
    - SEC climate disclosure rules
    """)
    
    # Regulation selection
    regulations = st.multiselect(
        "Select applicable regulations:",
        ["CSRD - EU", "GRI Standards", "SEC Climate Rule", "SASB Standards", "TCFD Recommendations"],
        default=["CSRD - EU", "GRI Standards"]
    )
    
    if st.button("Map Regulations", key="map_regulations"):
        with st.spinner("Mapping data to regulations with Regulation Decoder Agent..."):
            time.sleep(2)
            
            # Mock mapping results
            st.session_state.compliance_data['regulation_mapping'] = {
                'CSRD - EU': {
                    'required_fields': 47,
                    'available_fields': 38,
                    'compliance_percentage': 81
                },
                'GRI Standards': {
                    'required_fields': 52,
                    'available_fields': 49,
                    'compliance_percentage': 94
                }
            }
        
        st.success("✅ Data successfully mapped to regulations!")
        st.session_state.current_step = 2
        
        # Display mapping results
        st.subheader("Mapping Results")
        for reg, details in st.session_state.compliance_data['regulation_mapping'].items():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(f"{reg} - Total Requirements", details['required_fields'])
            with col2:
                st.metric(f"{reg} - Available Data", details['available_fields'])
            with col3:
                st.metric(f"{reg} - Compliance %", f"{details['compliance_percentage']}%")

def compliance_analysis():
    st.header("Step 3: Compliance Analysis")
    
    st.write("""
    The Compliance Checker Agent performs gap analysis and risk assessment:
    - Identifies compliance gaps
    - Calculates risk scores
    - Prioritizes remediation
    """)
    
    if st.button("Analyze Compliance", key="analyze_compliance"):
        with st.spinner("Analyzing compliance with Compliance Checker Agent..."):
            time.sleep(2)
            
            # Mock analysis results
            st.session_state.compliance_data['compliance_assessment'] = {
                'risk_score': 24,
                'gaps': [
                    {'requirement': 'Scope 3 emissions reporting', 'impact': 'High', 'risk': 8.5},
                    {'requirement': 'Biodiversity impact assessment', 'impact': 'Medium', 'risk': 6.2},
                    {'requirement': 'Supply chain due diligence', 'impact': 'High', 'risk': 7.8}
                ],
                'recommendations': [
                    'Implement Scope 3 emissions tracking system',
                    'Engage biodiversity consultant for impact assessment',
                    'Strengthen supplier ESG requirements'
                ]
            }
        
        st.success("✅ Compliance analysis completed!")
        st.session_state.current_step = 3
        
        # Display results
        assessment = st.session_state.compliance_data['compliance_assessment']
        
        st.subheader("Risk Assessment")
        st.metric("Overall Risk Score", assessment['risk_score'], "Out of 100")
        
        st.subheader("Compliance Gaps")
        for i, gap in enumerate(assessment['gaps']):
            with st.container():
                st.write(f"**{i+1}. {gap['requirement']}**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"Impact: **{gap['impact']}**")
                with col2:
                    st.write(f"Risk: **{gap['risk']}/10**")
                with col3:
                    if gap['risk'] > 7:
                        st.error("High Risk")
                    elif gap['risk'] > 4:
                        st.warning("Medium Risk")
                    else:
                        st.info("Low Risk")
        
        st.subheader("Recommendations")
        for rec in assessment['recommendations']:
            st.info(f"💡 {rec}")

def generate_report():
    st.header("Step 4: Generate Report")
    
    st.write("""
    The Report Drafting Agent creates comprehensive compliance reports in multiple formats:
    - Executive summary
    - Detailed compliance assessment
    - Remediation plan
    """)
    
    # Report format selection
    formats = st.multiselect(
        "Select report formats:",
        ["PDF", "Excel", "Word", "JSON"],
        default=["PDF", "Excel"]
    )
    
    if st.button("Generate Compliance Report", key="generate_report"):
        with st.spinner("Generating report with Report Drafting Agent..."):
            time.sleep(3)
            
            # Mock report generation
            st.session_state.report_generated = True
        
        st.success("✅ Compliance report generated successfully!")
    
    if st.session_state.report_generated:
        st.subheader("Compliance Report Summary")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.write("**Compliance Status**")
            st.metric("", "87%", "Overall")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.write("**Risk Reduction**")
            st.metric("", "76%", "from baseline")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.write("**Time Savings**")
            st.metric("", "40x", "faster reporting")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Executive Summary")
        st.write("""
        The ESG Compliance Co-Pilot has completed a comprehensive analysis of your ESG data against 
        selected regulatory frameworks. The system has identified key compliance gaps and provided 
        risk assessments and remediation recommendations.
        """)
        
        st.write("""
        Key findings include:
        - 87% overall compliance with selected regulations
        - 24% overall risk score (improved from 100% baseline)
        - Top risks in Scope 3 emissions, biodiversity impact, and supply chain due diligence
        - Recommended remediation actions are provided
        """)
        
        # Download buttons
        st.subheader("Download Reports")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Sample PDF report
            import base64
            pdf_bytes = b"This is a sample compliance report. In the full implementation, this would contain detailed analysis, charts, and recommendations."
            b64_pdf = base64.b64encode(pdf_bytes).decode()
            href_pdf = f'<a href="data:application/pdf;base64,{b64_pdf}" download="compliance_report.pdf">Download PDF Report</a>'
            st.markdown(href_pdf, unsafe_allow_html=True)
        
        with col2:
            # Sample Excel report
            df = pd.DataFrame({
                'Requirement': ['Scope 1 Emissions', 'Scope 2 Emissions', 'Scope 3 Emissions', 'Water Usage', 'Waste Management'],
                'Compliance': ['Yes', 'Yes', 'No', 'Yes', 'Partially'],
                'Risk': ['Low', 'Low', 'High', 'Medium', 'Medium'],
                'Recommendations': ['Maintain tracking', 'Maintain tracking', 'Implement system', 'Monitor usage', 'Improve recycling']
            })
            excel_bytes = BytesIO()
            with pd.ExcelWriter(excel_bytes, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            excel_bytes.seek(0)
            
            b64_excel = base64.b64encode(excel_bytes.getvalue()).decode()
            href_excel = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_excel}" download="compliance_report.xlsx">Download Excel Report</a>'
            st.markdown(href_excel, unsafe_allow_html=True)
        
        with col3:
            # Sample Word report
            doc_bytes = b"This is a sample Word report. In the full implementation, this would be a properly formatted Word document with sections for executive summary, detailed findings, and recommendations."
            b64_doc = base64.b64encode(doc_bytes).decode()
            href_doc = f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64_doc}" download="compliance_report.docx">Download Word Report</a>'
            st.markdown(href_doc, unsafe_allow_html=True)
        
        # Full implementation details
        st.subheader("How It Works")
        st.write("""
        The ESG Compliance Co-Pilot uses a four-agent architecture powered by IBM watsonx Orchestrate:
        
        1. **Data Hunter Agent**: Collects ESG data from your enterprise systems (ERP, HRIS, Finance)
        2. **Regulation Decoder Agent**: Maps data to specific compliance requirements across multiple frameworks
        3. **Compliance Checker Agent**: Identifies gaps and calculates risk scores
        4. **Report Drafting Agent**: Generates comprehensive reports in multiple formats
        """)
        
        # Reset button
        if st.button("Start New Analysis"):
            st.session_state.current_step = 0
            st.session_state.compliance_data = {}
            st.session_state.report_generated = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()