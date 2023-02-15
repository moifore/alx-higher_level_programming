-- Lists all cities of California found in database hbtn_0d_usa
SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN states AS s ON c.state_id ORDER BY c.id;
