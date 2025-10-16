-- MySQL schema for KOE Inventory demo
CREATE DATABASE IF NOT EXISTS koe_inventory;
USE koe_inventory;

CREATE TABLE IF NOT EXISTS employees (
    employee_id VARCHAR(36) PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    department VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS assets (
    asset_id VARCHAR(36) PRIMARY KEY,
    tag VARCHAR(64) UNIQUE,
    name VARCHAR(255),
    type VARCHAR(100),
    serial VARCHAR(100),
    status VARCHAR(50),
    assigned_to VARCHAR(36),
    FOREIGN KEY (assigned_to) REFERENCES employees(employee_id)
);

-- Sample data (replace or extend as needed)
INSERT INTO employees (employee_id, full_name, department) VALUES
('emp-1','Ayşe Yilmaz','Manufacturing'),
('emp-2','Mehmet Oz','Logistics'),
('emp-3','Fatma Kara','Quality'),
('emp-4','Ali Demir','Maintenance'),
('emp-5','Zeynep Aydin','HR');

INSERT INTO assets (asset_id, tag, name, type, serial, status, assigned_to) VALUES
('asset-1','KOE-001','Lenovo Laptop','Laptop','SN-LEN-001','active','emp-1'),
('asset-2','KOE-002','iPhone 12','Mobile','SN-IPH-002','active','emp-2'),
('asset-3','KOE-003','Logitech Mouse','Mouse','SN-MOU-003','maintenance','emp-3'),
('asset-4','KOE-004','Dell Monitor','Monitor','SN-MON-004','maintenance','emp-4'),
('asset-5','KOE-005','HP Keyboard','Keyboard','SN-KBD-005','inactive','emp-5');
