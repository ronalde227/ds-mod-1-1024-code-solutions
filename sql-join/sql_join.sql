use telecom;

select * from train;
select * from severity_type;
select * from log_feature;

SELECT t.id, t.location, t.fault_severity, et.event_type,
		st.severity_type, rt.resource_type, lf.log_feature, lf.volume
FROM train t
	LEFT OUTER JOIN severity_type st
	ON t.id = st.id
	LEFT OUTER JOIN resource_type rt
	on rt.id = t.id
	LEFT OUTER JOIN log_feature lf
	on lf.id = t.id
	LEFT OUTER JOIN event_type et
	on et.id = t.id;