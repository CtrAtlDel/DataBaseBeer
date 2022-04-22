CREATE TYPE beer_container AS ENUM ('bottle', 'barrel', 'tank', 'keg');
CREATE TYPE type_institution AS ENUM ('restaurant', 'bar', 'snack-bar');
CREATE TYPE status_institution AS ENUM ('the best', 'middle', 'not so bad');
CREATE TYPE status_half_part AS ENUM ('inBrewery', 'inWareHouse', 'inInstitution');
CREATE TYPE type_of_payment AS ENUM ('cash', 'online');
CREATE DOMAIN type_phone_number AS varchar(10)
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
    name       varchar(10)                      NOT NULL
        CONSTRAINT empty_name CHECK ( "Brewery".name != '' ),
    country    varchar(10)                      NOT NULL
        CONSTRAINT empty_country CHECK ( "Brewery".country != '' ),
    year       INT                              NOT NULL
        CONSTRAINT positive_year CHECK ( "Brewery".year > 0 ),
    PRIMARY KEY (id_brewery)
);

CREATE TABLE IF NOT EXISTS "Sort" -- ???
(
    id_sort   INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    sort_name varchar(20) UNIQUE               NOT NULl,
    PRIMARY KEY (id_sort)
);
CREATE UNIQUE INDEX sort_name_indx ON "Sort" (lower(sort_name));

CREATE TABLE IF NOT EXISTS "SortBrewery" -- ??? fk unique?
(
    id_sort    INT        NOT NULL,
    id_brewery INT UNIQUE NOT NULL,

    CONSTRAINT fk1 FOREIGN KEY (id_sort) REFERENCES "Sort" (id_sort)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk2 FOREIGN KEY (id_brewery) REFERENCES "Brewery" (id_brewery)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "SupplyAgreement"
(
    agreement_id        SERIAL          NOT NULL UNIQUE PRIMARY KEY,
    id_order            INT             NOT NULL,
    CONSTRAINT fk FOREIGN KEY (id_order) REFERENCES "Order" (id_order)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    name_beer           varchar(20)     NOT NULL,
    container           beer_container  NOT NULL,
    count_of_beer       INT             NOT NULL CHECK (count_of_beer > 0),
    cost                MONEY           NOT NULL,
    start_date          DATE            NOT NULL,
    account_number      varchar(20)     NOT NULL,
    prepayment          MONEY           NOT NULL CHECK (prepayment > 0),

    name_of_institution varchar(20)     NOT NULL,


    delivery_period     INTERVAL        NOT NULL,
    count_of_delivery   INT             NOT NULL
        CONSTRAINT positive_count CHECK ( count_of_delivery > 0 ),
    pay                 type_of_payment NOT NULL DEFAULT 'cash',

    isImporter          BOOLEAN                  DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS "Check"
(
    id_check       SERIAL UNIQUE NOT NULL PRIMARY KEY,

    id_agreement   INT UNIQUE    NOT NULL,
    CONSTRAINT fk FOREIGN KEY (id_agreement) REFERENCES "SupplyAgreement" (agreement_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    account_number varchar(20)   NOT NULL,
    sum            INT           NOT NULL
        CONSTRAINT positive_check CHECK ( "Check".sum > 0 )
);

CREATE TABLE IF NOT EXISTS "Order"
(
    id_order       INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    id_institution INT                              NOT NULL,
    CONSTRAINT fk FOREIGN KEY (id_institution) REFERENCES "Institution" (id_institution)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    all_sum        INT                              NOT NULL,               -- Вся сумма
    counter_half   INT                              NOT NULL DEFAULT 0,     -- Количество частей
    isAllPayed     BOOLEAN                                   DEFAULT FALSE, --  Оплачено ли все
    PRIMARY KEY (id_order)
);

CREATE TABLE IF NOT EXISTS "HalfOrder"
(
    order_id    INT              NOT NULL,
    CONSTRAINT fk FOREIGN KEY (order_id) REFERENCES "Order"
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    half        INT              NOT NULL               -- какая пр счету часть
        CONSTRAINT positive_half CHECK ( half > 0 ),
    all_size    INT              NOT NULL               -- все части
        CONSTRAINT positive_all_size CHECK ( all_size > 0 AND all_size > half ),
    tracking    status_half_part NOT NULL DEFAULT 'inBrewery',

    isHalfPayed BOOLEAN                   DEFAULT FALSE -- часть оплачна
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

CREATE TABLE IF NOT EXISTS "Invoice"
(
    id_invoice   INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    id_order     INT UNIQUE                       NOT NULL,
    id_brewery   INT                              NOT NULL,
    id_part      INT UNIQUE                       NOT NULL,

    CONSTRAINT fk1
        FOREIGN KEY (id_order) REFERENCES "Order" (id_order)
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

    name_of_beer varchar(15)                      NOT NULL,
    container    beer_container                   NOT NULL,
    count        int
        CONSTRAINT empty_count CHECK ( "Invoice".count > 0 ) DEFAULT 1,
    price        int                              NOT NULL
        CONSTRAINT negative_price CHECK ( "Invoice".price > 0 ),
    data         DATE                             NOT NULL
);
CREATE INDEX data_indx ON "Invoice" (data);

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
    "drink-ability" varchar(255)   NOT NULL,
    description     text           NOT NULL,
    color           varchar(255)   NOT NULL,
    strength        int            NOT NULL DEFAULT 0,
    volume          int            NOT NUll,
    price_purchase  int            NOT NULL
        CONSTRAINT positive_purchase CHECK ( "Beer".price_purchase > 0 ),
    price_selling   int            NOT NULL
        CONSTRAINT positive_selling CHECK ( "Beer".price_selling > 0 ),
    price_wholesale int            NOT NULL
        CONSTRAINT positive_wholesale CHECK ( "Beer".price_wholesale > 0),
    sort            varchar(20)    NOT NULL,

    PRIMARY KEY (id_beer)
);
CREATE UNIQUE INDEX beer_index ON "Beer" (name_of_beer);