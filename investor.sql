SELECT  total_invested.investorId, ((total_loss.total*1.00)/(total_invested.total*1.00))*100
AS defrate
FROM total_invested
JOIN total_loss
ON total_loss.investorId = total_invested.investorId
GROUP BY total_invested.investorId
HAVING total_invested.total > 10
ORDER BY defrate
DESC