from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # للسماح للواجهة بالتواصل مع الخادم

# ضع مفتاح API الخاص بك هنا للاختبار المحلي فقط
genai.configure(api_key="AQ.Ab8RN6IYQG5RCxv3jyGFBC6f1Y6n5ewVLhprzxoojgi6WYLLIw")
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/api/judge', methods=['POST'])
def judge_code():
    data = request.json
    code = data.get('code')
    language = data.get('language')
    
    # تلقين القاضي السيبراني
    system_prompt = f"""
    أنت قاضٍ سيبراني قاسٍ وساخر. المتهم قدم كوداً بلغة {language}:
    {code}
    اسخر من الكود، حدد الأخطاء بوضوح، ثم اطلب 'عقوبة برمجية' بسيطة يجب على المتهم برمجتها قبل أن تعطيه الحل.
    """
    
    try:
        response = model.generate_content(system_prompt)
        return jsonify({"verdict": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)