from sqlalchemy import text


class SecurityRepository:

    def __init__(self, engine):
        self.engine = engine

    def upsert(self, dataframe):

        query = text("""
        INSERT INTO SecurityMaster
        (
            SecurityID,
            SecurityName
        )
        VALUES
        (
            :securityid,
            :securityname
        )
        ON CONFLICT (SecurityID)
        DO UPDATE
        SET
            SecurityName = EXCLUDED.SecurityName;
        """)

        with self.engine.begin() as conn:

            for _, row in dataframe.iterrows():

                conn.execute(
                    query,
                    {
                        "securityid": int(row["securityid"]),
                        "securityname": row["securityname"]
                    }
                )

        print(f"✓ {len(dataframe)} securities imported.")