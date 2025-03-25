import mysql.connector as sql

class UserManager:
    def __init__(self, db_config):
        self.db_config = db_config
    
    def _connect(self):
        # print(self.db_config)
        return sql.connect(**self.db_config)

    def reg_user(self, discord_id: int, discord_name: str, display_name: str | None) -> str:
        
        connection = None
        cursor = None
        mention = f"<@{discord_id}>"
        display = display_name_safe = display_name if display_name else discord_name

        # Attempt to establish a connection
        try:
            connection = self._connect()
            cursor = connection.cursor()
        
            # Check if the user exists
            cursor.execute("SELECT * FROM fx_users WHERE discord_id = %s", (discord_id,))
        
            if cursor.fetchone():
                cursor.execute(
                    "UPDATE fx_users SET display_name = %s WHERE discord_id = %s",
                    (display, discord_id)
                )
                connection.commit()
                return f"✅ Updated display name for {mention} to {display}!"

            # Insert new user
            cursor.execute(
                "INSERT INTO fx_users (discord_id, display_name) VALUES (%s, %s)",
                (discord_id, display)
            )
            connection.commit()
            return f"✅ Registered {mention} as {display} successfully!"

        except sql.Error as err:
            print(f"MySQL Error: {err}")
            return "❌ Unexcepted Database Error!"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def set_channel_name(self, discord_id: int, channel_name: str | None):
        
        connection = None
        cursor = None
        mention = f"<@{discord_id}>"
        user_id = 0

        # Attempt to establish a connection
        try:
            connection = self._connect()
            cursor = connection.cursor()
        
            # Check if the user exists
            cursor.execute("SELECT * FROM fx_users WHERE discord_id = %s", (discord_id,))
            row = cursor.fetchone()

            if row:
                user_id = row[0]
                channel = channel_name if channel_name else f"{row[2]}\'s channel" 
            else:
                return f"❌ {mention} you are not yet registered!"
            
            cursor.execute("SELECT * FROM fx_user_channel_name WHERE user_id = %s", (user_id,))

            if cursor.fetchone():
                cursor.execute(
                    "UPDATE fx_user_channel_name SET channel_name = %s WHERE user_id = %s",
                    (channel, user_id)
                )
                connection.commit()
                return f"✅ Updated channel name for {mention} to {channel}!"

            # Insert new channel name
            cursor.execute(
                "INSERT INTO fx_user_channel_name (user_id, channel_name) VALUES (%s, %s)",
                (user_id, channel)
            )
            connection.commit()
            return f"✅ Registered {channel} for {mention} successfully!"

        except sql.Error as err:
            print(f"MySQL Error: {err}")
            return "❌ Unexcepted Database Error!"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
