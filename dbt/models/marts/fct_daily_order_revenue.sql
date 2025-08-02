select
o.order_id,
o.order_date,
sum(total_price) as total_price
from
{{ref('stg_orders')}} o
left join
{{ref('stg_order_items')}} oi
on 
o.ORDER_ID=oi.ORDER_ID
group by 1,2

