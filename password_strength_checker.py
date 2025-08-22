import re
import streamlit as st

# ---------- Password Check Functions ----------
def password_length(passwd):
    return len(passwd) >= 8

def password_strength(passwd):
    strength = 0
    suggestions = []

    if re.search(r"[A-Z]", passwd):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", passwd):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    if re.search(r"\d", passwd):
        strength += 1
    else:
        suggestions.append("Add at least one number")

    if re.search(r"\W", passwd):
        strength += 1
    else:
        suggestions.append("Add at least one special character")

    return strength, suggestions


def cracking_time(passwd):
    r = 0
    length = len(passwd)

    if re.search(r"[a-z]", passwd):
        r += 26 ** length
    if re.search(r"[A-Z]", passwd):
        r += 26 ** length
    if re.search(r"\d", passwd):
        r += 10 ** length
    if re.search(r"\W", passwd):
        r += 31 ** length

    if r == 0:
        return None, "Invalid password"

    time_in_seconds = r / 1_000_000_000

    if time_in_seconds < 60:
        return time_in_seconds, f"{time_in_seconds:.2f} seconds"
    elif time_in_seconds < 3600:
        return time_in_seconds, f"{time_in_seconds//60:.0f} minutes"
    elif time_in_seconds < 86400:
        return time_in_seconds, f"{time_in_seconds//3600:.0f} hours"
    elif time_in_seconds < 604800:
        return time_in_seconds, f"{time_in_seconds//86400:.0f} days"
    elif time_in_seconds < 2592000:
        return time_in_seconds, f"{time_in_seconds//604800:.0f} weeks"
    elif time_in_seconds < 31536000:
        return time_in_seconds, f"{time_in_seconds//2592000:.0f} months"
    else:
        return time_in_seconds, f"{time_in_seconds//31536000:.0f} years"


def password_rating(time_in_seconds):
    if time_in_seconds < 3600:
        return "🔴 Very Weak"
    elif time_in_seconds < 86400:
        return "🟠 Weak"
    elif time_in_seconds < 604800:
        return "🟡 Moderate"
    elif time_in_seconds < 7257600:
        return "🟢 Strong"
    else:
        return "🟣 Very Strong"


# ---------- Streamlit UI ----------
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Checker")
st.write("Check your password strength and estimated cracking time.")

passwd = st.text_input("Enter a password", type="password")

if passwd:
    if " " in passwd:
        st.error("❌ Spaces are not allowed in password.")
    else:
        # Check length
        if not password_length(passwd):
            st.warning("⚠️ Password must be at least 8 characters")

        # Strength
        strength, suggestions = password_strength(passwd)
        st.subheader("Password Strength")
        st.progress(strength / 4)

        labels = ["Uppercase", "Lowercase", "Number", "Special Char"]
        st.write(f"**Strength Level:** {strength}/4")

        if suggestions:
            st.info("🔧 Suggestions to improve:")
            for s in suggestions:
                st.write(f"- {s}")

        # Cracking time
        time_sec, crack_time = cracking_time(passwd)
        if time_sec:
            st.subheader("Estimated Cracking Time")
            st.success(f"⏳ {crack_time}")

            # Rating
            rating = password_rating(time_sec)
            st.markdown(f"### Strength Rating: {rating}")
