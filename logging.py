import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def log_user_activity(user_id, activity):
    logging.info(f'User {user_id} performed {activity}')

log_user_activity(123, 'login')
log_user_activity(123, 'viewed profile')