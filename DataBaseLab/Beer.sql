CREATE TYPE beer_container AS ENUM ('bottle', 'barrel', 'tank', 'keg');
CREATE TYPE type_institution AS ENUM ('restaurant', 'bar', 'snack-bar');
CREATE TYPE status_institution AS ENUM ('the best', 'middle', 'not so bad');
CREATE TYPE status_half_part AS ENUM ('inBrewery', 'inWareHouse', 'inInstitution');
CREATE TYPE type_of_payment AS ENUM ('cash', 'online');
CREATE DOMAIN type_phone_number AS varchar(20)
    CHECK (
        VALUE ~ '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
        );


CREATE TABLE IF NOT EXISTS "Institution"
(
    id_institution INT GENERATED ALWAYS AS IDENTITY NOT NULL,

    name           varchar(20)                      NOT NULL
        CONSTRAINT empty_column CHECK ( name != '' ),
    address        varchar(20)                      NOT NULL
        CONSTRAINT empty_address CHECK ( "Institution".address != '' ),
    phone_number   type_phone_number                NOT NULL
        CONSTRAINT empty_phone_number CHECK ( "Institution".phone_number != ''),
    type           type_institution                 NOT NULL,
    status         status_institution               NOT NULL,
    PRIMARY KEY (id_institution)
);
CREATE UNIQUE INDEX name_indx ON "Institution" (lower(name));

INSERT INTO "Institution" (name, address, phone_number, type, status)
VALUES ('Nora Cafe', 'Not address', '+79099090990', 'bar', 'middle'),
       ('Cafe Parisienne', 'Not address', '+79099090990', 'bar', 'middle'),
       ('Devine', 'Not address', '+79099090990', 'bar', 'middle'),
       ('Tanias of Hampstead', 'Not address', '+79099090990', 'bar', 'middle'),
       ('Kennington Lane Cafe', 'Not address', '+79099090990', 'bar', 'middle');


CREATE TABLE IF NOT EXISTS "WareHouse"
(
    id_wareHouse    INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    university_code char(10)                         NOT NULL
        CONSTRAINT empty_code CHECK ( "WareHouse".university_code != '' ),
    address         varchar(30)                      NOT NULL
        CONSTRAINT empty_address CHECK ( "WareHouse".address != '' ),
    capacity        int                              NOT NULL DEFAULT 10,
    phone_number    type_phone_number                NOT NULL
        CONSTRAINT empty_phone_number CHECK ("WareHouse".phone_number != ''),
    boss            varchar(20)                      NOT NULL,
    information     varchar(1000)                    NOT NULL,
    coordinates     point                            NOT NULL,

    PRIMARY KEY (id_wareHouse)
);
CREATE UNIQUE INDEX wareHouse_number_indx ON "WareHouse" (phone_number);
CREATE INDEX wareHouse_code_indx ON "WareHouse" (lower(university_code));

INSERT INTO "WareHouse" (university_code, address, capacity, phone_number, boss, information, coordinates)
VALUES ('0000', 'some address', 400, '+79095045090', 'Oleg', 'not info', '(10,20)');
INSERT INTO "WareHouse" (university_code, address, capacity, phone_number, boss, information, coordinates)
VALUES ('0001', 'some address', 500, '+79999999999', 'Boris', 'not info', '(15,10)'),
       ('0010', 'bad address', 600, '+79090400200', 'Olga', 'not info too', '(90, 100)');

CREATE TABLE IF NOT EXISTS "InstitutionWarehouse"
(
    id_wareHouse   INT UNIQUE NOT NULL,
    id_institution INT        NOT NULL,
    CONSTRAINT fk1
        FOREIGN KEY (id_wareHouse)
            REFERENCES "WareHouse" (id_wareHouse)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,
    CONSTRAINT fk2
        FOREIGN KEY (id_institution)
            REFERENCES "Institution" (id_institution)
            ON DELETE RESTRICT
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Brewery"
(
    id_brewery INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    name       varchar(20)                      NOT NULL
        CONSTRAINT empty_name CHECK ( "Brewery".name != '' ),
    country    varchar(20)                      NOT NULL
        CONSTRAINT empty_country CHECK ( "Brewery".country != '' ),
    year       INT                              NOT NULL
        CONSTRAINT positive_year CHECK ( "Brewery".year > 0 ),
    PRIMARY KEY (id_brewery)
);

INSERT INTO "Brewery" (name, country, year)
VALUES ('Beartown', 'Cheshire', 2000),
       ('Beavertown', 'London', 1999),
       ('Bedlam', 'West Sussex', 1998),
       ('Beer Brothers', 'Lancashire', 1999);

CREATE TABLE IF NOT EXISTS "Sort"
(
    id_sort   INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    sort_name varchar(20) UNIQUE               NOT NULl,
    PRIMARY KEY (id_sort)
);
CREATE UNIQUE INDEX sort_name_indx ON "Sort" (lower(sort_name));

INSERT INTO "Sort"(sort_name)
VALUES ('Ale'),
       ('Lager'),
       ('Porter');


CREATE TABLE IF NOT EXISTS "SortBrewery"
(
    id_sort    INT NOT NULL,
    id_brewery INT NOT NULL,

    CONSTRAINT fk1 FOREIGN KEY (id_sort) REFERENCES "Sort" (id_sort)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk2 FOREIGN KEY (id_brewery) REFERENCES "Brewery" (id_brewery)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    UNIQUE (id_sort, id_brewery)
);

INSERT INTO "SortBrewery"(id_sort, id_brewery)
VALUES ('1', '1'),
       ('1', '2'),
       ('1', '3'),
       ('2', '1'),
       ('2', '3');



CREATE TABLE IF NOT EXISTS "SupplyAgreement"
(
    id_agreement        INT GENERATED ALWAYS AS IDENTITY NOT NULL,

    id_institution      INT                              NOT NULL,
    CONSTRAINT fk1 FOREIGN KEY (id_institution) REFERENCES "Institution" (id_institution)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,


    name_beer           varchar(20)                      NOT NULL,
    container           beer_container                   NOT NULL,
    count_of_beer       INT                              NOT NULL CHECK (count_of_beer > 0),
    cost                MONEY                            NOT NULL,
    start_date          DATE                             NOT NULL,
    account_number      varchar(20)                      NOT NULL,
    prepayment          MONEY                            NOT NULL,

    name_of_institution varchar(20)                      NOT NULL,


    delivery_period     INTERVAL                         NOT NULL,
    count_of_delivery   INT                              NOT NULL
        CONSTRAINT positive_count CHECK ( count_of_delivery > 0 ),
    pay                 type_of_payment                  NOT NULL DEFAULT 'cash',

    isImporter          BOOLEAN                                   DEFAULT FALSE,
    PRIMARY KEY (id_agreement)
);

INSERT INTO "SupplyAgreement"(id_institution, name_beer, container, count_of_beer, cost, start_date, account_number,
                              prepayment, name_of_institution, delivery_period, count_of_delivery)
VALUES ('1', 'QWert', 'tank', 400, 50, '1997-08-24', '20', '30', 'bab', '40:00:00', 20);

CREATE TABLE IF NOT EXISTS "Check"
(
    id_check       INT GENERATED ALWAYS AS IDENTITY NOT NULL,

    id_agreement   INT UNIQUE                       NOT NULL,
    CONSTRAINT fk FOREIGN KEY (id_agreement) REFERENCES "SupplyAgreement" (id_agreement)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    account_number varchar(20)                      NOT NULL,
    sum            INT                              NOT NULL
        CONSTRAINT positive_check CHECK ( "Check".sum > 0 ),

    PRIMARY KEY (id_check)
);

CREATE TABLE IF NOT EXISTS "Orders"
(
    id_order     INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    agreement_id INT                              NOT NULL,

    all_sum      INT                              NOT NULL
        CONSTRAINT positive_size CHECK ( all_sum > 0),                -- Вся сумма
    all_count    INT                              NOT NULL DEFAULT 0, -- Количество частей


    half         INT                              NOT NULL            -- какая по счету часть
        CONSTRAINT positive_half CHECK ( half > 0 ),
    all_half     INT                              NOT NULL            -- все части
        CONSTRAINT positive_all_size CHECK ( all_half > 0 AND all_half > half ),
    tracking     status_half_part                 NOT NULL DEFAULT 'inBrewery',

    isHalfPayed  BOOLEAN                                   DEFAULT FALSE,
    isAllPayed   BOOLEAN
                                                           DEFAULT FALSE,

    CONSTRAINT fk2 FOREIGN KEY (agreement_id) REFERENCES "SupplyAgreement" (id_agreement)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    PRIMARY KEY (id_order)
);

CREATE TABLE IF NOT EXISTS "Part"
(
    id_part    INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    id_brewery INT                              NOT NULL,
    CONSTRAINT fk1 FOREIGN KEY (id_brewery) REFERENCES "Brewery" (id_brewery)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    size_part  int                              NOT NUll CHECK ( "Part".size_part > 0 ),
    PRIMARY KEY (id_part)
);
CREATE OR REPLACE PROCEDURE create_part(idInvoice integer)
    LANGUAGE plpgsql
AS
$$
DECLARE
    cur          refcursor;
    beer_name    varchar(20);
    id_brew  int;
BEGIN
    OPEN cur FOR SELECT * FROM "Beer" WHERE "Beer".id_beer = beer_name;
    FETCH cur INTO beer_name;
    SELECT "Brewery".id_brewery INTO id_brew
    FROM "Brewery"
             JOIN "Sort" AS S ON sort_name = beer_name--in (SELECT "Beer".sort FROM "Beer" WHERE "Beer".id_beer = beer_name)
             JOIN "SortBrewery"  AS SB ON SB.id_sort = S.id_sort
             JOIN "Brewery" AS B ON "Brewery".id_brewery =  SB.id_brewery;

    INSERT INTO "Part"(id_brewery, size_part) VALUES (id_brew, 4);
END
$$;

INSERT INTO "Part" (id_brewery, size_part)
VALUES ('1', 4),
       ('2', 5),
       ('3', 6),
       ('4', 7),
       ('2', 6);


CREATE TABLE IF NOT EXISTS "HalfPart"
(
    id_wareHouse INT NOT NULL,
    CONSTRAINT fk1 FOREIGN KEY (id_wareHouse) REFERENCES "WareHouse" (id_wareHouse)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    id_part      INT NOT NULL REFERENCES "Part" (id_part)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    id_brewery   INT NOT NULL REFERENCES "Brewery" (id_brewery)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    size_half    int NOT NULL CHECK ( "HalfPart".size_half > 0) DEFAULT 1
);

INSERT INTO "HalfPart" (id_wareHouse, id_part, id_brewery, size_half)
VALUES ('1', '1', '1', 1);

INSERT INTO "HalfPart" (id_wareHouse, id_part, id_brewery, size_half)
VALUES ('2', '1', '1', 5);

INSERT INTO "HalfPart" (id_wareHouse, id_part, id_brewery, size_half)
VALUES ('2', '10', '1', 1);


CREATE OR REPLACE FUNCTION partions_check()
    RETURNS TRIGGER AS
$$
DECLARE
    belong record;
BEGIN
    IF NEW.size_half >= 3 THEN
        RAISE EXCEPTION 'Bad size of half partition';
        RETURN NULL;
    end if;

    SELECT id_brewery INTO belong FROM "Part" WHERE id_part = NEW.id_part;

    IF belong.id_brewery != NEW.id_brewery THEN
        RAISE EXCEPTION 'Bad size of half partition';
        RETURN NULL;
    END IF;

    IF NEW.size_half < 3 THEN
        RETURN NEW;
    end if;
END
$$ LANGUAGE plpgsql;

DROP TRIGGER partions_check on "HalfPart";
CREATE TRIGGER partions_check
    BEFORE INSERT OR UPDATE
    ON "HalfPart"
    FOR EACH ROW
EXECUTE PROCEDURE partions_check();


CREATE TABLE IF NOT EXISTS "Invoice"
(
    id_invoice   INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    id_order     INT,
    id_brewery   INT,
    id_part      INT,
    id_agreement INT                              NOT NULL,

    CONSTRAINT fk1
        FOREIGN KEY (id_order) REFERENCES "Orders" (id_order)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,

    CONSTRAINT fk2
        FOREIGN KEY (id_brewery) REFERENCES "Brewery" (id_brewery)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,

    CONSTRAINT fk3
        FOREIGN KEY (id_part) REFERENCES "Part" (id_part)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,

    CONSTRAINT fk4
        FOREIGN KEY (id_agreement) REFERENCES "SupplyAgreement" (id_agreement)
            ON DELETE RESTRICT
            On UPDATE CASCADE,

    name_of_beer varchar(15)                      NOT NULL,
    container    beer_container                   NOT NULL,
    count        int
        CONSTRAINT empty_count CHECK ( "Invoice".count > 0 ) DEFAULT 1,
    price        money                            NOT NULL,
    data         DATE                             NOT NULL
);
CREATE INDEX data_indx ON "Invoice" (data);

CREATE OR REPLACE PROCEDURE insert_ivoice(idAgreements integer)
    LANGUAGE plpgsql
AS
$$
DECLARE
    solution       int;
    name_beer      varchar(20);
    containers     beer_container;
    count_of_beer  int;
    cost           MONEY ;
    start_date     DATE ;
    account_number varchar(20) ;
    prepayment     MONEY ;
begin
    SELECT "SupplyAgreement".id_agreement,
           "SupplyAgreement".name_beer,
           "SupplyAgreement".container,
           "SupplyAgreement".count_of_beer,
           "SupplyAgreement".cost,
           "SupplyAgreement".start_date,
           "SupplyAgreement".account_number,
           "SupplyAgreement".prepayment
    INTO solution,
        name_beer,
        containers,
        count_of_beer,
        cost,
        start_date,
        account_number,
        prepayment
    FROM "SupplyAgreement"
    WHERE "SupplyAgreement".id_agreement = $1;

    IF NOT EXISTS(SELECT id_agreement
                  FROM "SupplyAgreement"
                  WHERE id_agreement = $1) then
        RAISE EXCEPTION 'Cannot find this supId';
    END IF;

    INSERT INTO "Invoice" (id_order, ID_PART, ID_AGREEMENT, NAME_OF_BEER, CONTAINER, COUNT, PRICE, data)
    VALUES (NULL, NULL, solution, name_beer, containers, count_of_beer, cost, start_date);

end
$$;

CALL insert_ivoice(1);
CALL insert_ivoice(2);

CREATE TABLE IF NOT EXISTS "Beer"
(
    id_beer         INT GENERATED ALWAYS AS IDENTITY,
    id_part         INT            NOT NULL,
    CONSTRAINT fk1 FOREIGN KEY (id_part) REFERENCES "Part" (id_part)
        ON DELETE NO ACTION
        ON UPDATE RESTRICT,

    id_brewery      INT            NOT NULL,
    CONSTRAINT fk2 FOREIGN KEY (id_brewery) REFERENCES "Brewery" (id_brewery)
        ON DELETE NO ACTION
        ON UPDATE RESTRICT,

    name_of_beer    varchar(15)    NOT NULL,
    container       beer_container NOT NULL,
    drinkAbility    varchar(255)   NOT NULL,
    description     varchar(255),
    color           varchar(255)   NOT NULL,
    strength        int            NOT NULL DEFAULT 0,
    volume          int            NOT NUll,
    price_purchase  int            NOT NULL -- цена закупки
        CONSTRAINT positive_purchase CHECK ( "Beer".price_purchase > 0 ),
    price_selling   int            NOT NULL -- цена оптовой продажи
        CONSTRAINT positive_selling CHECK ( "Beer".price_selling > 0 ),
    price_wholesale int            NOT NULL -- цена розничной продажи
        CONSTRAINT positive_wholesale CHECK ( "Beer".price_wholesale > 0),
    sort            varchar(20)    NOT NULL,

    PRIMARY KEY (id_beer)
);
CREATE UNIQUE INDEX beer_index ON "Beer" (name_of_beer);

INSERT INTO "Beer"(id_part, id_brewery, name_of_beer, container, drinkAbility, description, color, strength, volume,
                   price_purchase, price_selling, price_wholesale, sort)
VALUES ('1', '1', 'Essa', 'tank', 'Very tasty beer', 'qwer', 'bright', '5', '100', '3', '4', '5', 'sds');

INSERT INTO "Beer"(id_part, id_brewery, name_of_beer, container, drinkAbility, description, color, strength, volume,
                   price_purchase, price_selling, price_wholesale, sort)
VALUES ('1', '1', 'QWert', 'tank', 'Very tasty beer', 'qwer', 'bright', '5', '100', '3', '4', '5', 'Ale');



