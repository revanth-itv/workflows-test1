if cd /home/revanth/rick && '.git/' in ls -Fa | grep -q .git/
	if 'workflows-test1' in cd /home/revanth/rick && git config --get remote.origin.url
	then
		cd /home/revanth/rick && git pull origin master
	fi
else
	cd /home/revanth/rick && git init
	cd /home/revanth/rick && git remote add origin git@github.com:revanth-itv/workflows-test1.git
	cd /home/revanth/rick && git pull origin master
fi

