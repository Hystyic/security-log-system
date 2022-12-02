TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER `resident_insertion` BEFORE INSERT ON `resident` FOR EACH ROW BEGIN\nDECLARE error_msg VARCHAR(255);\nSET error_msg = (\'Cannot allocate more tenancy\');\nIF (New.resident_id ) > 255\nTHEN\nSIGNAL SQLSTATE \'45000\'\nSET MESSAGE_TEXT = error_msg; \nEND IF;\nEND'
sql_modes=1098907648
definers='root@localhost'
client_cs_names='utf8mb4'
connection_cl_names='utf8mb4_unicode_ci'
db_cl_names='utf8mb4_general_ci'
created=166990794983
