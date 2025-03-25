USE fangxiatech_discord;

CREATE TABLE IF NOT EXISTS fx_users (

    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    discord_id BIGINT NOT NULL UNIQUE,
    display_name VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS fx_user_channel_name (
    
    user_id BIGINT PRIMARY KEY,
    channel_name VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES fx_users(user_id)
        ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS fx_user_privileges (

    user_id BIGINT PRIMARY KEY,

    beta_test_privilege BOOLEAN,

    admin_privilege BOOLEAN,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES fx_users(user_id)
        ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS fx_user_vc (

    channel_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    discord_channel_id BIGINT,

    user_id BIGINT UNIQUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES fx_users(user_id)
        ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS fx_user_channel_privileges (

    channel_id BIGINT PRIMARY KEY,

    user_id BIGINT,
    guest_discord_id BIGINT,

    black_list BOOLEAN NOT NULL,
    white_list BOOLEAN NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (channel_id) REFERENCES fx_user_vc(channel_id)
        ON DELETE CASCADE

);
