.DEFAULT_GOAL := make

build_compose:
	sed -f conf_subst.sed docker-compose.yaml.in > docker-compose.yaml

clean:
	@if [ -f "docker-compose.yaml" ]; then\
		rm docker-compose.yaml; \
	fi;

rise_and_shine: build_compose
	docker-compose up --build

down:
	docker-compose down

make: rise_and_shine
