# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cql.cqltypes import cql_types

class CQLHelpTopics(object):
    def get_help_topics(self):
        return [ t[5:] for t in dir(self) if t.startswith('help_') ]

    def print_help_topic(self, topic):
        getattr(self, 'help_' + topic.lower())()

    def help_types(self):
        print "\n        CQL types recognized by this version of cqlsh:\n"
        for t in cql_types:
            print '          ' + t
        print """
        For information on the various recognizable input formats for these
        types, or on controlling the formatting of cqlsh query output, see
        one of the following topics:

          HELP TIMESTAMP_INPUT
          HELP BLOB_INPUT
          HELP UUID_INPUT
          HELP BOOLEAN_INPUT

          HELP TEXT_OUTPUT
          HELP TIMESTAMP_OUTPUT
        """

    def help_timestamp_input(self):
        print """
        Timestamp input

        CQL supports any of the following ISO 8601 formats for timestamp
        specification:

          yyyy-mm-dd HH:mm
          yyyy-mm-dd HH:mm:ss
          yyyy-mm-dd HH:mmZ
          yyyy-mm-dd HH:mm:ssZ
          yyyy-mm-dd'T'HH:mm
          yyyy-mm-dd'T'HH:mmZ
          yyyy-mm-dd'T'HH:mm:ss
          yyyy-mm-dd'T'HH:mm:ssZ
          yyyy-mm-dd
          yyyy-mm-ddZ

        The Z in these formats refers to an RFC-822 4-digit time zone,
        expressing the time zone's difference from UTC. For example, a
        timestamp in Pacific Standard Time might be given thus:

          2012-01-20 16:14:12-0800

        If no time zone is supplied, the current time zone for the Cassandra
        server node will be used.
        """

    def help_blob_input(self):
        print """
        Blob input

        CQL blob data must be specified in a string literal as hexidecimal
        data. Example: to store the ASCII values for the characters in the
        string "CQL", use '43514c'.
        """

    def help_uuid_input(self):
        print """
        UUID input

        UUIDs may be specified in CQL using 32 hexidecimal characters,
        split up using dashes in the standard UUID format:

          XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
        """

    def help_boolean_input(self):
        print """
        Boolean input

        CQL accepts the strings 'true' and 'false' (case insensitive)
        as input for boolean types.
        """

    def help_timestamp_output(self):
        print """
        Timestamp output

        Cqlsh will display timestamps in the following format by default:

          yyyy-mm-dd HH:mm:ssZ

        which is a format acceptable as CQL timestamp input as well.
        The output format can be changed by setting 'time_format' property
        in the [ui] section of .cqlshrc file.
        """

    def help_text_output(self):
        print """
        Textual output

        When control characters, or other characters which can't be encoded
        in your current locale, are found in values of 'text' or 'ascii'
        types, it will be shown as a backslash escape. If color is enabled,
        any such backslash escapes will be shown in a different color from
        the surrounding text.

        Unicode code points in your data will be output intact, if the
        encoding for your locale is capable of decoding them. If you prefer
        that non-ascii characters be shown with Python-style "\\uABCD"
        escape sequences, invoke cqlsh with an ASCII locale (for example,
        by setting the $LANG environment variable to "C").
        """
    help_ascii_output = help_text_output

    def help_create_index(self):
        print """
        CREATE INDEX [<indexname>] ON <cfname> ( <colname> );

        A CREATE INDEX statement is used to create a new, automatic secondary
        index on the given CQL table, for the named column. A name for the
        index itself can be specified before the ON keyword, if desired. A
        single column name must be specified inside the parentheses. It is not
        necessary for the column to exist on any current rows (Cassandra is
        schema-optional), but the column must already have a type (specified
        during the CREATE TABLE, or added afterwards with ALTER TABLE).
        """

    def help_drop(self):
        print """
        There are different variants of DROP. For more information, see
        one of the following:

          HELP DROP_KEYSPACE;
          HELP DROP_TABLE;
          HELP DROP_INDEX;
        """

    def help_drop_keyspace(self):
        print """
        DROP KEYSPACE <keyspacename>;

        A DROP KEYSPACE statement results in the immediate, irreversible
        removal of a keyspace, including all column families in it, and all
        data contained in those column families.
        """

    def help_drop_table(self):
        print """
        DROP TABLE <tablename>;

        A DROP TABLE statement results in the immediate, irreversible
        removal of a CQL table and the underlying column family, including all
        data contained in it.
        """
    help_drop_columnfamily = help_drop_table

    def help_drop_index(self):
        print """
        DROP INDEX <indexname>;

        A DROP INDEX statement is used to drop an existing secondary index.
        """

    def help_truncate(self):
        print """
        TRUNCATE <tablename>;

        TRUNCATE accepts a single argument for the table name, and permanently
        removes all data from it.
        """

    def help_create(self):
        print """
        There are different variants of CREATE. For more information, see
        one of the following:

          HELP CREATE_KEYSPACE;
          HELP CREATE_TABLE;
          HELP CREATE_INDEX;
        """

    def help_use(self):
        print """
        USE <keyspacename>;

        Tells cqlsh and the connected Cassandra instance that you will be
        working in the given keyspace. All subsequent operations on tables
        or indexes will be in the context of this keyspace, unless otherwise
        specified, until another USE command is issued or the connection
        terminates.

        As always, when a keyspace name does not work as a normal identifier or
        number, it can be quoted using single quotes (CQL 2) or double quotes
        (CQL 3).
        """

    def help_create_table(self):
        print """
        CREATE TABLE <cfname> ( <colname> <type> PRIMARY KEY [,
                                <colname> <type> [, ...]] )
               [WITH <optionname> = <val> [AND <optionname> = <val> [...]]];

        CREATE TABLE statements create a new CQL table under the current
        keyspace. Valid table names are strings of alphanumeric characters and
        underscores, which begin with a letter.

        Each table requires a primary key, which will correspond to the
        underlying columnfamily key and key validator. It's important to
        note that the key type you use must be compatible with the partitioner
        in use. For example, OrderPreservingPartitioner and
        CollatingOrderPreservingPartitioner both require UTF-8 keys.

        In cql3 mode, a table can have multiple columns composing the primary
        key (see HELP COMPOSITE_PRIMARY_KEYS).

        For more information, see one of the following:

          HELP CREATE_TABLE_TYPES;
          HELP CREATE_TABLE_OPTIONS;
        """
    help_create_columnfamily = help_create_table

    def help_create_table_types(self):
        print """
        CREATE TABLE: Specifying column types

          CREATE ... (KEY <type> PRIMARY KEY,
                      othercol <type>) ...

        It is possible to assign columns a type during table creation. Columns
        configured with a type are validated accordingly when a write occurs,
        and intelligent CQL drivers and interfaces will be able to decode the
        column values correctly when receiving them. Column types are specified
        as a parenthesized, comma-separated list of column term and type pairs.
        See HELP TYPES; for the list of recognized types.
        """
    help_create_columnfamily_types = help_create_table_types

    def help_create_table_options(self):
        print """
        CREATE TABLE: Specifying columnfamily options

          CREATE TABLE blah (...)
             WITH optionname = val AND otheroption = val2;

        A number of optional keyword arguments can be supplied to control the
        configuration of a new CQL table, such as the size of the associated
        row and key caches for the underlying Cassandra columnfamily. Consult
        your CQL reference for the complete list of options and possible
        values.
        """
    help_create_columnfamily_options = help_create_table_options

    def help_alter(self):
        print """
        ALTER TABLE <tablename> ALTER <columnname> TYPE <type>;
        ALTER TABLE <tablename> ADD <columnname> <type>;
        ALTER TABLE <tablename> DROP <columnname>;
        ALTER TABLE <tablename> WITH <optionname> = <val> [AND <optionname> = <val> [...]];

        An ALTER statement is used to manipulate table metadata. It allows you
        to add new typed columns, drop existing columns, change the data
        storage type of existing columns, or change table properties.
        No results are returned.

        See one of the following for more information:

          HELP ALTER_ALTER;
          HELP ALTER_ADD;
          HELP ALTER_DROP;
          HELP ALTER_WITH;
        """

    def help_alter_alter(self):
        print """
        ALTER TABLE: altering existing typed columns

          ALTER TABLE addamsFamily ALTER lastKnownLocation TYPE uuid;

        ALTER TABLE ... ALTER changes the expected storage type for a column.
        The column must already have a type in the column family metadata. The
        column may or may not already exist in current rows-- but be aware that
        no validation of existing data is done. The bytes stored in values for
        that column will remain unchanged, and if existing data is not
        deserializable according to the new type, this may cause your CQL
        driver or interface to report errors.
        """

    def help_alter_add(self):
        print """
        ALTER TABLE: adding a typed column

          ALTER TABLE addamsFamily ADD gravesite varchar;

        The ALTER TABLE ... ADD variant adds a typed column to a column
        family. The column must not already have a type in the column family
        metadata. See the warnings on HELP ALTER_ALTER regarding the lack of
        validation of existing data; they apply here as well.
        """

    def help_alter_drop(self):
        print """
        ALTER TABLE: dropping a typed column

          ALTER TABLE addamsFamily DROP gender;

        An ALTER TABLE ... DROP statement removes the type of a column
        from the column family metadata. Note that this does _not_ remove the
        column from current rows; it just removes the metadata saying that the
        bytes stored under that column are expected to be deserializable
        according to a certain type.
        """

    def help_alter_with(self):
        print """
        ALTER TABLE: changing column family properties

          ALTER TABLE addamsFamily WITH comment = 'Glad to be here!'
                                    AND read_repair_chance = 0.2;

        An ALTER TABLE ... WITH statement makes adjustments to the
        table properties, as defined when the table was created (see
        HELP CREATE_TABLE_OPTIONS and your Cassandra documentation for
        information about the supported parameter names and values).
        """

    def help_delete_columns(self):
        print """
        DELETE: specifying columns

          DELETE col1, col2, col3 FROM ...

        Following the DELETE keyword is an optional comma-delimited list of
        column name terms. When no column names are given, the remove applies
        to the entire row(s) matched by the WHERE clause.

        When column names do not parse as valid CQL identifiers, they can be
        quoted in single quotes (CQL 2) or double quotes (CQL 3).
        """

    def help_delete_where(self):
        print """
        DELETE: specifying rows

          DELETE ... WHERE keycol = 'some_key_value';
          DELETE ... WHERE keycol1 = 'val1' AND keycol2 = 'val2';
          DELETE ... WHERE keycol IN (key1, key2);

        The WHERE clause is used to determine to which row(s) a DELETE
        applies. The first form allows the specification of a precise row
        by specifying a particular primary key value (if the primary key has
        multiple columns, values for each must be given). The second form
        allows a list of key values to be specified using the IN operator
        and a parenthesized list of comma-delimited key values.
        """

    def help_update_set(self):
        print """
        UPDATE: Specifying Columns and Row

          UPDATE ... SET name1 = value1, name2 = value2
                   WHERE <key> = keyname;
          UPDATE ... SET name1 = value1, name2 = value2
                   WHERE <key> IN ('<key1>', '<key2>', ...)

        Rows are created or updated by supplying column names and values in
        term assignment format.  Multiple columns can be set by separating the
        name/value pairs using commas.
        """

    def help_update_counters(self):
        print """
        UPDATE: Updating Counter Columns

          UPDATE ... SET name1 = name1 + <value> ...
          UPDATE ... SET name1 = name1 - <value> ...

        Counter columns can be incremented or decremented by an arbitrary
        numeric value though the assignment of an expression that adds or
        substracts the value.
        """

    def help_update_where(self):
        print """
        UPDATE: Selecting rows to update

          UPDATE ... WHERE <keyname> = <keyval>;
          UPDATE ... WHERE <keyname> IN (<keyval1>, <keyval2>, ...);
          UPDATE ... WHERE <keycol1> = <keyval1> AND <keycol2> = <keyval2>;

        Each update statement requires a precise set of keys to be specified
        using a WHERE clause.

        If the table's primary key consists of multiple columns, an explicit
        value must be given for each for the UPDATE statement to make sense.
        """

    def help_select_table(self):
        print """
        SELECT: Specifying Table

          SELECT ... FROM [<keyspace>.]<tablename> ...

        The FROM clause is used to specify the CQL table applicable to a SELECT
        query. The keyspace in which the table exists can optionally be
        specified along with the table name, separated by a dot (.). This will
        not change the current keyspace of the session (see HELP USE).
        """
    help_select_columnfamily = help_select_table

    def help_select_where(self):
        print """
        SELECT: Filtering rows

          SELECT ... WHERE <key> = keyname AND name1 = value1
          SELECT ... WHERE <key> >= startkey and <key> =< endkey AND name1 = value1
          SELECT ... WHERE <key> IN ('<key>', '<key>', '<key>', ...)

        The WHERE clause provides for filtering the rows that appear in
        results.  The clause can filter on a key name, or range of keys, and in
        the case of indexed columns, on column values.  Key filters are
        specified using the KEY keyword or key alias name, a relational
        operator (one of =, >, >=, <, and <=), and a term value.  When terms
        appear on both sides of a relational operator it is assumed the filter
        applies to an indexed column. With column index filters, the term on
        the left of the operator is the name, the term on the right is the
        value to filter _on_.

        Note: The greater-than and less-than operators (> and <) result in key
        ranges that are inclusive of the terms. There is no supported notion of
        "strictly" greater-than or less-than; these operators are merely
        supported as aliases to >= and <=.
        """

    def help_select_limit(self):
        print """
        SELECT: Limiting results

          SELECT ... WHERE <clause> [LIMIT n] ...

        Limiting the number of rows returned can be achieved by adding the
        LIMIT option to a SELECT expression. LIMIT defaults to 10,000 when left
        unset.
        """

class CQL2HelpTopics(CQLHelpTopics):
    def help_create_keyspace(self):
        print """
        CREATE KEYSPACE <ksname> WITH strategy_class = '<strategy>'
                                 [AND strategy_options:<option> = <val>];

        The CREATE KEYSPACE statement creates a new top-level namespace (aka
        "keyspace"). Valid names are any string constructed of alphanumeric
        characters and underscores. Names which do not work as valid
        identifiers or integers should be quoted as string literals. Properties
        such as replication strategy and count are specified during creation
        using the following accepted keyword arguments:

          strategy_class [required]: The name of the replication strategy class
          which should be used for the new keyspace. Some often-used classes
          are SimpleStrategy and NetworkTopologyStrategy.

          strategy_options: Most strategies require additional arguments which
          can be supplied by appending the option name to "strategy_options",
          separated by a colon (:). For example, a strategy option of "DC1"
          with a value of "1" would be specified as "strategy_options:DC1 = 1".
          The replication factor option for SimpleStrategy could be
          "strategy_options:replication_factor=3".
        """

    def help_begin(self):
        print """
        BEGIN BATCH [USING CONSISTENCY <level>
                       [AND TIMESTAMP <timestamp>]]
          <insert or update or delete statement> ;
          [ <another insert or update or delete statement ;
            [...]]
        APPLY BATCH;

        BATCH supports setting a client-supplied optional global timestamp
        which will be used for each of the operations included in the batch.

        A single consistency level is used for the entire batch. It appears
        after the BEGIN BATCH statement, and uses the standard "consistency
        level specification" (see HELP CONSISTENCYLEVEL). Batched statements
        default to CONSISTENCY.ONE when left unspecified.

        Only data modification statements (specifically, UPDATE, INSERT,
        and DELETE) are allowed in a BATCH statement. BATCH is _not_ an
        analogue for SQL transactions.

        _NOTE: While there are no isolation guarantees, UPDATE queries are
        atomic within a given record._
        """
    help_apply = help_begin

    def help_select(self):
        print """
        SELECT [FIRST n] [REVERSED] <selectExpr>
          FROM [<keyspace>.]<table>
            [USING CONSISTENCY <consistencylevel>]
            [WHERE <clause>]
            [ORDER BY <colname> [DESC]]
            [LIMIT m];

        SELECT is used to read one or more records from a CQL table. It returns
        a set of rows matching the selection criteria specified.

        Note that FIRST and REVERSED are only supported in CQL 2, and ORDER BY
        is only supported in CQL 3 and higher.

        For more information, see one of the following:

          HELP SELECT_EXPR
          HELP SELECT_TABLE
          HELP SELECT_WHERE
          HELP SELECT_LIMIT
          HELP CONSISTENCYLEVEL
        """

    def help_delete(self):
        print """
        DELETE [<col1> [, <col2>, ...] FROM [<keyspace>.]<tablename>
               [USING CONSISTENCY <consistencylevel>
                   [AND TIMESTAMP <timestamp>]]
            WHERE <keyname> = <keyvalue>;

        A DELETE is used to perform the removal of one or more columns from one
        or more rows. Each DELETE statement requires a precise set of row keys
        to be specified using a WHERE clause and the KEY keyword or key alias.

        For more information, see one of the following:

          HELP DELETE_USING
          HELP DELETE_COLUMNS
          HELP DELETE_WHERE
          HELP CONSISTENCYLEVEL
        """

    def help_delete_using(self):
        print """
        DELETE: the USING clause

          DELETE ... USING CONSISTENCY <consistencylevel>;
          DELETE ... USING TIMESTAMP <timestamp>;

        The USING clause allows setting of certain query and data parameters.
        If multiple parameters need to be set, these may be joined using AND.
        Example:

          DELETE ... CONSISTENCY LOCAL_QUORUM AND TIMESTAMP 1318452291034;

        <timestamp> defines the optional timestamp for the new tombstone
        record. It must be an integer. Cassandra timestamps are generally
        specified using milliseconds since the Unix epoch (1970-01-01 00:00:00
        UTC).
        """

    def help_update(self):
        print """
        UPDATE [<keyspace>.]<columnFamily>
                              [USING CONSISTENCY <consistencylevel>
                                [AND TIMESTAMP <timestamp>]
                                [AND TTL <timeToLive>]]
               SET name1 = value1, name2 = value2 WHERE <keycol> = keyval;

        An UPDATE is used to write one or more columns to a record in a table.
        No results are returned. The record's primary key must be completely
        and uniquely specified; that is, if the primary key includes multiple
        columns, all must be explicitly given in the WHERE clause.

        Statements begin with the UPDATE keyword followed by the name of the
        table to be updated.

        For more information, see one of the following:

          HELP UPDATE_USING
          HELP UPDATE_SET
          HELP UPDATE_COUNTERS
          HELP UPDATE_WHERE
          HELP CONSISTENCYLEVEL
        """

    def help_update_using(self):
        print """
        UPDATE: the USING clause

          UPDATE ... USING TIMESTAMP <timestamp>;
          UPDATE ... USING TTL <timeToLive>;
          UPDATE ... USING CONSISTENCY <consistencylevel>;

        The USING clause allows setting of certain query and data parameters.
        If multiple parameters need to be set, these may be joined using AND.
        Example:

          UPDATE ... USING TTL 43200 AND CONSISTENCY LOCAL_QUORUM;

        <timestamp> defines the optional timestamp for the new column value(s).
        It must be an integer. Cassandra timestamps are generally specified
        using milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

        <timeToLive> defines the optional time to live (TTL) in seconds for the
        new column value(s). It must be an integer.
        """

    def help_consistencylevel(self):
        print """
        Consistency Level Specification

          ... USING CONSISTENCY <consistencylevel> ...

        Consistency level specifications are made up of keyword USING,
        followed by a consistency level identifier. Valid consistency level
        identifiers are as follows:

         * ANY
         * ONE (default)
         * TWO
         * THREE
         * QUORUM
         * ALL
         * LOCAL_QUORUM
         * EACH_QUORUM

        For more information on how consistency levels work, consult your
        Cassandra documentation.
        """

    def help_insert(self):
        print """
        INSERT INTO [<keyspace>.]<tablename>
                    ( <colname1>, <colname2> [, <colname3> [, ...]] )
               VALUES ( <colval1>, <colval2> [, <colval3> [, ...]] )
               [USING CONSISTENCY <consistencylevel>
                 [AND TIMESTAMP <timestamp>]
                 [AND TTL <timeToLive>]];

        An INSERT is used to write one or more columns to a record in a
        CQL table. No results are returned.

        Values for all component columns in the table's primary key must
        be given. Also, there must be at least one non-primary-key column
        specified (Cassandra rows are not considered to exist with only
        a key and no associated columns).

        Unlike in SQL, the semantics of INSERT and UPDATE are identical.
        In either case a record is created if none existed before, and
        udpated when it does. For more information, see one of the
        following:

          HELP UPDATE
          HELP UPDATE_USING
          HELP CONSISTENCYLEVEL
        """

    def help_select_expr(self):
        print """
        SELECT: Specifying Columns

          SELECT [FIRST n] [REVERSED] name1, name2, name3 FROM ...
          SELECT [FIRST n] [REVERSED] name1..nameN FROM ...
          SELECT COUNT(*) FROM ...

        The SELECT expression determines which columns will appear in the
        results and takes the form of either a comma separated list of names,
        or a range. The range notation consists of a start and end column name
        separated by two periods (..). The set of columns returned for a
        range is start and end inclusive.

        The FIRST option accepts an integer argument and can be used to apply a
        limit to the number of columns returned per row.  When this limit is
        left unset, it defaults to 10,000 columns.

        The REVERSED option causes the sort order of the results to be
        reversed.

        It is worth noting that unlike the projection in a SQL SELECT, there is
        no guarantee that the results will contain all of the columns
        specified. This is because Cassandra is schema-less and there are no
        guarantees that a given column exists.

        When the COUNT aggregate function is specified as a column to fetch, a
        single row will be returned, with a single column named "count" whose
        value is the number of rows from the pre-aggregation resultset.

        Currently, COUNT is the only function supported by CQL.

         ** [FIRST n] and [REVERSED] are no longer supported in CQL 3.
        """

class CQL3HelpTopics(CQLHelpTopics):
    def help_create_keyspace(self):
        print """
        CREATE KEYSPACE <ksname>
            WITH replication = {'class':'<strategy>' [,'<option>':<val>]};

        The CREATE KEYSPACE statement creates a new top-level namespace (aka
        "keyspace"). Valid names are any string constructed of alphanumeric
        characters and underscores. Names which do not work as valid
        identifiers or integers should be quoted as string literals. Properties
        such as replication strategy and count are specified during creation
        as key-value pairs in the 'replication' map:

          class [required]: The name of the replication strategy class
          which should be used for the new keyspace. Some often-used classes
          are SimpleStrategy and NetworkTopologyStrategy.

          other options [optional]: Most strategies require additional arguments
          which can be supplied as key-value pairs in the 'replication' map.

        Examples:

          To create a keyspace with NetworkTopologyStrategy and strategy option of "DC1"
          with a value of "1" and "DC2" with a value of "2" you would use
          the following statement:
            CREATE KEYSPACE <ksname>
                WITH replication = {'class':'NetworkTopologyStrategy', 'DC1':1, 'DC2':2};

         To create a keyspace with SimpleStrategy and "replication_factor" option
         with a value of "3" you would use this statement:
            CREATE KEYSPACE <ksname>
                WITH replication = {'class':'SimpleStrategy', 'replication_factor':3};
        """

    def help_begin(self):
        print """
        BEGIN [UNLOGGED|COUNTER] BATCH [USING TIMESTAMP <timestamp>]
          <insert or update or delete statement> ;
          [ <another insert or update or delete statement ;
            [...]]
        APPLY BATCH;

        BATCH supports setting a client-supplied optional global timestamp
        which will be used for each of the operations included in the batch.

        Only data modification statements (specifically, UPDATE, INSERT,
        and DELETE) are allowed in a BATCH statement. BATCH is _not_ an
        analogue for SQL transactions.

        _NOTE: Counter mutations are allowed only within COUNTER batches._

        _NOTE: While there are no isolation guarantees, UPDATE queries are
        atomic within a given record._
        """
    help_apply = help_begin

    def help_select(self):
        print """
        SELECT <selectExpr>
          FROM [<keyspace>.]<table>
            [WHERE <clause>]
            [ORDER BY <colname> [DESC]]
            [LIMIT m];

        SELECT is used to read one or more records from a CQL table. It returns
        a set of rows matching the selection criteria specified.

        For more information, see one of the following:

          HELP SELECT_EXPR
          HELP SELECT_TABLE
          HELP SELECT_WHERE
          HELP SELECT_LIMIT
        """

    def help_delete(self):
        print """
        DELETE [<col1> [, <col2>, ...] FROM [<keyspace>.]<tablename>
               [USING TIMESTAMP <timestamp>]
            WHERE <keyname> = <keyvalue>;

        A DELETE is used to perform the removal of one or more columns from one
        or more rows. Each DELETE statement requires a precise set of row keys
        to be specified using a WHERE clause and the KEY keyword or key alias.

        For more information, see one of the following:

          HELP DELETE_USING
          HELP DELETE_COLUMNS
          HELP DELETE_WHERE
        """

    def help_delete_using(self):
        print """
        DELETE: the USING clause

          DELETE ... USING TIMESTAMP <timestamp>;

        <timestamp> defines the optional timestamp for the new tombstone
        record. It must be an integer. Cassandra timestamps are generally
        specified using milliseconds since the Unix epoch (1970-01-01 00:00:00
        UTC).
        """

    def help_update(self):
        print """
        UPDATE [<keyspace>.]<columnFamily>
                              [USING [TIMESTAMP <timestamp>]
                                [AND TTL <timeToLive>]]
               SET name1 = value1, name2 = value2 WHERE <keycol> = keyval;

        An UPDATE is used to write one or more columns to a record in a table.
        No results are returned. The record's primary key must be completely
        and uniquely specified; that is, if the primary key includes multiple
        columns, all must be explicitly given in the WHERE clause.

        Statements begin with the UPDATE keyword followed by the name of the
        table to be updated.

        For more information, see one of the following:

          HELP UPDATE_USING
          HELP UPDATE_SET
          HELP UPDATE_COUNTERS
          HELP UPDATE_WHERE
        """

    def help_update_using(self):
        print """
        UPDATE: the USING clause

          UPDATE ... USING TIMESTAMP <timestamp>;
          UPDATE ... USING TTL <timeToLive>;

        The USING clause allows setting of certain query and data parameters.
        If multiple parameters need to be set, these may be joined using AND.
        Example:

          UPDATE ... USING TTL 43200 AND TIMESTAMP 1351620509603

        <timestamp> defines the optional timestamp for the new column value(s).
        It must be an integer. Cassandra timestamps are generally specified
        using milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

        <timeToLive> defines the optional time to live (TTL) in seconds for the
        new column value(s). It must be an integer.
        """

    def help_insert(self):
        print """
        INSERT INTO [<keyspace>.]<tablename>
                    ( <colname1>, <colname2> [, <colname3> [, ...]] )
               VALUES ( <colval1>, <colval2> [, <colval3> [, ...]] )
               [USING TIMESTAMP <timestamp>]
                 [AND TTL <timeToLive]];

        An INSERT is used to write one or more columns to a record in a
        CQL table. No results are returned.

        Values for all component columns in the table's primary key must
        be given. Also, there must be at least one non-primary-key column
        specified (Cassandra rows are not considered to exist with only
        a key and no associated columns).

        Unlike in SQL, the semantics of INSERT and UPDATE are identical.
        In either case a record is created if none existed before, and
        udpated when it does. For more information, see one of the
        following:

          HELP UPDATE
          HELP UPDATE_USING
        """

    def help_select_expr(self):
        print """
        SELECT: Specifying Columns

          SELECT name1, name2, name3 FROM ...
          SELECT COUNT(*) FROM ...

        The SELECT expression determines which columns will appear in the
        results and takes the form of a comma separated list of names.

        It is worth noting that unlike the projection in a SQL SELECT, there is
        no guarantee that the results will contain all of the columns
        specified. This is because Cassandra is schema-less and there are no
        guarantees that a given column exists.

        When the COUNT aggregate function is specified as a column to fetch, a
        single row will be returned, with a single column named "count" whose
        value is the number of rows from the pre-aggregation resultset.

        Currently, COUNT is the only function supported by CQL.
        """