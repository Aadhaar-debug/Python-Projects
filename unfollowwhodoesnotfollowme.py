from instagrapi import Client
import time

# Your Instagram credentials
USERNAME = "Username"
PASSWORD = "Password"

SESSION_FILE = "session.json"  # File to store session dataye
def login_to_instagram():
    """Logs in using a stored session or creates a new one."""
    cl = Client()
    try:
        cl.load_settings(SESSION_FILE)  # Try loading session
        cl.login(USERNAME, PASSWORD)
        print("✅ Logged in using session.")
    except Exception:
        print("⚠️ Session not found. Logging in fresh...")
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(SESSION_FILE)  # Save session for later use
        print("✅ New session saved.")
    return cl

def get_non_followers(cl, my_username):
    """Finds people I follow who don't follow me back."""
    user_id = cl.user_id_from_username(my_username)

    print("📌 Fetching followers...")
    time.sleep(3)
    followers = cl.user_followers(user_id)

    print("📌 Fetching following...")
    time.sleep(3)
    following = cl.user_following(user_id)

    # Convert to sets for easy comparison
    followers_set = set(followers.keys())  # Who follows me
    following_set = set(following.keys())  # Who I follow

    # Find non-followers (people I follow who don't follow me back)
    non_followers = following_set - followers_set

    # Debugging: Print raw data
    print(f"🔎 Debug: Found {len(non_followers)} non-followers.")

    # Fix: Ensure the user exists before trying to access 'username'
    non_followers_data = []
    for user_id in non_followers:
        if user_id in following:
            username = following[user_id].username
            non_followers_data.append((user_id, username))
        else:
            print(f"⚠️ Warning: Could not find username for user_id {user_id}")

    return non_followers_data

def unfollow_users(cl, non_followers):
    """Unfollows users who don't follow me back."""
    if not non_followers:
        print("🎉 You have no non-followers! Everyone you follow follows you back!")
        return

    print("\n🚨 Unfollowing users who don’t follow you back:")
    for user_id, username in non_followers:
        try:
            cl.user_unfollow(user_id)  # Unfollow the user
            print(f"❌ Unfollowed: {username}")
            time.sleep(5)  # Delay to prevent Instagram from blocking actions
        except Exception as e:
            print(f"⚠️ Could not unfollow {username}: {e}")
    
    print("✅ Done unfollowing non-followers!")

def logout_and_end_session(cl):
    """Logs out and ends the Instagram session."""
    try:
        cl.logout()
        print("🚪 Logged out successfully! Session ended.")
    except Exception as e:
        print(f"⚠️ Logout failed: {e}")

if __name__ == "__main__":
    cl = login_to_instagram()
    my_username = USERNAME  # Use your username
    
    try:
        non_followers = get_non_followers(cl, my_username)
        
        print("\n🚨 People I follow who don’t follow me back:")
        for _, user in non_followers:
            print(f"🔹 {user}")

        # Ask user before unfollowing
        confirm = input("\n⚠️ Do you want to unfollow these users? (yes/no): ").strip().lower()
        if confirm == "yes":
            unfollow_users(cl, non_followers)
        else:
            print("❌ Unfollow canceled.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        logout_and_end_session(cl)  # Ensure logout even if an error occurs
