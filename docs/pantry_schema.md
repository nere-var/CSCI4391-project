

| Name | Type | Description | Example |
|------|------|-------------|---------|
| id | INTEGER | auto-generated item number | 1 | 
| player_id | INTEGER | player item belongs to | 1 |
| name | TEXT | item name | tomato |
| category | TEXT | item category type | dairy |
| quantity | INTEGER | how many items | 1 |
| unit | TEXT | unit of measurement for item | g |
| measurment_type | TEXT | how was item measured | weight |
| quantity_grams | REAL | how many grams | 100.0 |
| quantity_ml | REAL | how many ml | 10.0 |
| purchase_date | TEXT | date item was purchased | 2026-02-10 |
| best_by | TEXT | expiry date | 2026-02-15 |
| raw_meat | BOOLEAN | is item raw | 1 |
| perishable | BOOLEAN | is item perishable | 1 |
| opened | BOOLEAN | is item open | 0 |
| donation_allowed | BOOLEAN | is item eligible for donation | 1 |
| price | REAL | price item purchased for | 2.49 |
| status | TEXT | status of item | active |

<br><br>
Canonicalization:<br>
When item values are case normalized(all lowercase) when entered into database.<br><br>
Allowed units:<br>
g, ml, cup, tbsp, pieces<br><br>
Expiration storage format:<br>
YYYY-MM-DD<br><br>
