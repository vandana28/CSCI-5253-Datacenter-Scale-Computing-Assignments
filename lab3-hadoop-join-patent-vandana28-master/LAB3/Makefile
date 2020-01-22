filesystem:
	-hdfs dfs -mkdir -p /user
	-hdfs dfs -mkdir -p /user/$(USER)

prepare:
	curl https://storage.googleapis.com/csci4253/acite75_99.zip > ~/acite75_99.zip
	unzip ~/acite75_99.zip -d ~/
	curl https://storage.googleapis.com/csci4253/apat63_99.zip > ~/apat63_99.zip
	unzip ~/apat63_99.zip -d ~/
	-hdfs dfs -mkdir input
	-hdfs dfs -put ~/cite75_99.txt /user/$(USER)/input
	-hdfs dfs -put ~/apat63_99.txt /user/$(USER)/input
    
stream:
	sh ./RUN-MAP-REDUCE
