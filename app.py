import openai
import streamlit as st

st.set_page_config(page_title="AI RTL Error Checker", layout="wide")
st.title("🧠 AI RTL Error Checker")
st.markdown("Upload your Verilog file to begin analysis.")

uploaded_file = st.file_uploader("Choose a Verilog (.v) file", type=["v"])

if uploaded_file is not None:
    verilog_code = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Uploaded Verilog Code:")
    st.code(verilog_code, language="verilog")

    # Basic analysis logic
    st.subheader("🔍 Basic Analysis:")
    if "module" in verilog_code and "endmodule" in verilog_code:
        st.success("✅ Code structure looks valid.")
    else:
        st.error("⚠️ Possible issue: missing 'module' or 'endmodule'.")
            # 🔍 AI-Powered Feedback
    st.subheader("🤖 AI Feedback:")

    import openai  # Make sure this is at the top of your file

    openai.api_key ="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"

    with st.spinner("Analyzing with AI..."):
        prompt = f"Analyze this Verilog code and suggest any syntax or logic errors:\n\n{verilog_code}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert in Verilog and RTL design."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )
            ai_feedback = response['choices'][0]['message']['content']
            st.success(ai_feedback)
        except Exception as e:
            st.error(f"AI analysis failed: {e}")
            st.header("🔄 FSM Generator from Natural Language")

fsm_description = st.text_area("Describe your FSM in plain English", placeholder="e.g., A 3-state FSM with IDLE, LOAD, and DONE states...")

if st.button("Generate FSM Verilog"):
    if fsm_description:
        prompt = f"Generate Verilog code for this FSM description:\n{fsm_description}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in Verilog and FSM design."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,
            temperature=0.3
        )
        fsm_code = response['choices'][0]['message']['content']
        st.subheader("🧠 Generated FSM Verilog Code:")
        st.code(fsm_code, language='verilog')
    else:
        st.warning("Please enter an FSM description.")
        st.header("🧪 AI Testbench Generator")

if uploaded_file is not None:
    if st.button("Generate Testbench"):
        prompt = f"Write a Verilog testbench for the following module:\n{verilog_code}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in Verilog testbench creation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,
            temperature=0.3
        )
        tb_code = response['choices'][0]['message']['content']
        st.subheader("🧪 Generated Testbench:")
        st.code(tb_code, language='verilog')
else:
    st.warning("Please upload a Verilog file to generate a testbench.")
