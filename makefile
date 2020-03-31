install:
	touch explore
	echo 'cd $(PWD)' > explore
	echo 'python3 $(PWD)/Explore.py' >> explore
	chmod +x explore
	echo 'export PATH="$(PWD):$$PATH"' >> $$HOME/.bashrc
	sudo pip3 install explore_package
	echo "Explore installed successfully!"

installpackage:
	sudo pip3 install explore-package/explore_package-2.0-py3-none-any.whl

buildpkg:
	python3 explore-package/setup.py bdist_wheel

installpkg:
	sudo pip3 uninstall explore_package
	sudo pip3 install explore-package/dist/explore_package-2.0-py3-none-any.whl

script:
	touch explore
	echo 'cd $(PWD)' > explore
	echo 'python3 $(PWD)/Explore.py' >> explore
	chmod +x explore

path:
	echo 'export PATH="$(PWD):$$PATH"' >> $$HOME/.bashrc

update:
	git pull

reset:
	rm .val .cipher log.txt
	clear
