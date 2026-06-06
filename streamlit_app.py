import streamlit as st

# 强制要求安装 google 依赖（Streamlit 后台会自动识别并安装）
try:
    import google.generativeai as genai
except ImportError:
    import os
    os.system('pip install google-generativeai')
    import google.generativeai as genai

# --- 1. 核心安全配置：把你的免费 API Key 锁在后台 ---
# 请将你在 Google AI Studio 申请的那一长串 API Key 替换掉下面的 "这里换成你的API_KEY"
# 比如：genai.configure(api_key="AIzaSyA1...")
genai.configure(api_key="genai.configure(api_key=st.secrets["GEMINI_API_KEY"])")

# 使用全免费且速度极快的 Gemini 1.5 Flash 引擎
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. 精美的前端 UI 包装（BMA 专属品牌定制） ---
st.set_page_config(page_title="BMA 价值投资操作系统", layout="centered")
st.title("The BMA Value Investing Framework")
st.write("---")
st.subheader("📊 请输入您想剖析的股票代码：")

# 前端唯一的输入框
stock_code = st.text_input("例如：TSLA, AAPL, NVDA", "")

if stock_code:
    with st.spinner("正在调用 BMA 核心主逻辑执行冷酷推演，请稍候..."):
        
        # --- 3. 铁壁防护：把你的投资底座和核心机密锁死在后端 ---
        system_instruction = f"""
        你现在是 BMA 价值投资核心AI。用户查询的股票代码是: {stock_code}
        
        【你的核心底座主逻辑与扣分规则】
        - 必须包含【模块三：仓位管理（资金配置建议）】：基于打分和 BMA 理念给出定性判断（甜蜜好球/昂贵核心资产/高风险投资盲盒/价值陷阱）与配置建议（0%观望、5-10%卫星投机/防守收息、15-20%核心底仓饱仓出击）。强调用堡垒级现金应对黑天鹅，绝不盲目加杠杆。
        - 必须包含【模块四：交易与参与周期界定】：长线复利底仓、忍受3-5年资本支出阵痛期的相变博弈、或等待估值泡沫挤出。并提出3条未来必须紧盯的核心信号（Checklist），一旦预警信号恶化，无论信仰多深，必须果断纠错止损。
        
        【动态个股最新数据区（未来有新研报和最新来源时，直接在下方追加一行即可）】
        - TSLA：最新一季FSD数据表现超预期，正在进入新旧经济融合相变期。
        - AAPL：服务费由于法案面临一定阵痛，但现金流壁垒依然稳固。
        
        【Output Format】
        - 语气要求：客观、冷静、犀利，不盲从市场情绪（拒绝FOMO），带有查理·芒格式的“毒舌”和阿贝尔式的“务实数据”风格。
        
        请严格基于以上框架，开始为 {stock_code} 输出深度剖析报告：
        """
        
        try:
            # 呼叫大模型免费生成
            response = model.generate_content(system_instruction)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"生成失败，请检查 API Key 配置。错误信息: {e}")
