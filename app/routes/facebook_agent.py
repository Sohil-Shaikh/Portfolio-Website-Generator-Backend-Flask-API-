# app/routes/facebook_agent.py
from flask import Blueprint, request, jsonify

fb_api = Blueprint('fb_api', __name__)

@fb_api.route('/facebook/plan', methods=['POST'])
def facebook_plan():
    data = request.get_json()
    url = data.get("url")
    industry = data.get("industry", "general")
    tone = data.get("tone", "friendly")
    freq = data.get("frequency", 2)
    post_mix = data.get("mix", ["tips", "promotions", "news"])

    mock_posts = {
        "tips": "Here’s a great tip to grow your business...",
        "promotions": "Enjoy 20% off this week!",
        "news": "Latest trends in your industry: AI is booming!"
    }

    days = ["Monday", "Wednesday", "Friday", "Sunday"]
    post_plan = []
    for i in range(freq):
        post_type = post_mix[i % len(post_mix)]
        post = f"[{tone.capitalize()}] {mock_posts[post_type]}"
        post_plan.append({"day": days[i], "post": post})

    return jsonify({"calendar": post_plan})
